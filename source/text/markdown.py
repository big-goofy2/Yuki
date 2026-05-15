class text:
  def __init__(self):
    self.lists = {}

  def bold(self,text):
    return f"\033[1m{text}\033[0m"

  def italic(self,text):
    return f"\x1B[3m{text}\x1B[0m"

  def bulletList(self, name,list_type="circle", content=None, indent=2, ordered=True):
    if name not in self.lists:
      self.lists[name] = {
        "items": content or [],
        "ordered": ordered,
        "indent": indent,
        "type": list_type
      }
      return self.render_list(name)

  def render_list(self, name):
    lst = self.lists[name]
    lines = []
    for i, item in enumerate(lst["items"], start=1):
      bullet = self.get_bullet(i, lst["type"])
      lines.append(" " * lst["indent"] + f"{bullet} {item}")
    return "\n".join(lines)

  def get_bullet(self, index, list_type):
    match list_type:
      case "number":
        return f"{index}."
      case "alpha":
        return f"{chr(96 + index)}."
      case "circle":
        return "●"
      case "arrow":
        return "➤"
      case "dash":
        return "-"
      case "star":
        return "★"
      case None:
        return "-"

  def add_item(self, name, item):
    self.lists[name]["items"].append(item)

  def edit_item(self, name, index, new_item):
    self.lists[name]["items"][index] = new_item

  def remove_item(self, name, index):
    self.lists[name]["items"].pop(index)

  def parse(self, text_input):
    original_text = text_input
    processed_text_for_comparison = original_text.lower()

    if processed_text_for_comparison.startswith("**") and processed_text_for_comparison.endswith("**"):
      inner_text = original_text[2:-2]
      return self.bold(inner_text)
    elif processed_text_for_comparison.startswith("*") and processed_text_for_comparison.endswith("*"):
      inner_text = original_text[1:-1]
      return self.italic(inner_text)
    else:
      return original_text
