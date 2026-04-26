import json
import os

class KnowledgeEngine:
    def __init__(self, data_path):
        with open(data_path, 'r') as f:
            data = json.load(f)
            self.tree = data['nodes']
            self.meta = data.get('metadata', {})
        self.state = {
            "axis1": {"internal": 0, "external": 0},
            "axis2": {"contribution": 0, "entitlement": 0},
            "axis3": {"self": 0, "altro": 0}
        }

    def get_node(self, node_id):
        return next((n for n in self.tree if n['id'] == node_id), None)

    def get_dominant(self, axis_key):
        scores = self.state[axis_key]
        return max(scores, key=scores.get)

    def calculate_persona(self):
        # High effort synthesis logic
        a1 = self.get_dominant("axis1")
        a2 = self.get_dominant("axis2")
        a3 = self.get_dominant("axis3")

        if a1 == "internal" and a3 == "altro":
            return "Catalyst (High Agency + High Team Focus)"
        if a1 == "internal" and a3 == "self":
            return "Solo Performer (High Agency + Individual Focus)"
        if a1 == "external":
            return "Passenger (Low Agency - Needs re-centering)"
        return "Standard Contributor"

    def render_chart(self):
        print("\n--- VISUAL GROWTH PROFILE ---")
        for axis, scores in self.state.items():
            total = sum(scores.values()) or 1
            dom = self.get_dominant(axis)
            percent = (scores[dom] / total) * 10
            bar = "█" * int(percent) + "░" * (10 - int(percent))
            print(f"{axis.upper():<10} | {bar} | {dom.capitalize()}")

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== {self.meta.get('title', 'Reflection Agent')} ===")
        current_id = "START"
        
        while current_id:
            node = self.get_node(current_id)
            if not node: break

            if node['type'] == 'summary':
                self.render_chart()
                text = node['text'].format(
                    axis1_dom=self.get_dominant("axis1"),
                    axis2_dom=self.get_dominant("axis2"),
                    axis3_dom=self.get_dominant("axis3"),
                    persona=self.calculate_persona()
                )
            else:
                text = node['text']

            print(f"\n[SYSTEM]: {text}")

            if node['type'] == 'end': break

            if node['type'] == 'question':
                for i, opt in enumerate(node['options']):
                    print(f"  {i+1}. {opt['text']}")
                
                try:
                    idx = int(input("\nSelection > ")) - 1
                    selected = node['options'][idx]
                    if 'signal' in selected:
                        axis, val = selected['signal'].split(':')
                        self.state[axis][val] += 1
                    current_id = selected['target']
                except:
                    print("Invalid input. Staying on current node.")
            else:
                input("\n(Enter to proceed...)")
                current_id = node.get('next')

if __name__ == "__main__":
    engine = KnowledgeEngine('../tree/reflection-tree.json')
    engine.run()