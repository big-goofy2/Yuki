import re

templates = {
    "function": "def {func_name}({args}):\n{body}\n    return {result}",
    "loop": "for {var} in {iterable}:\n{body}",
    "constant": "{var} = {expr}",
    "print": "print({target})",
    "check": "if {item}{check_op}{item2}:\n{body}",
    "get_module": "import {library_name}",
    "assign": "{var} = {value}"
}
feature_code = {
  "movement": """# Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_y -= speed
    if keys[pygame.K_s]: player_y += speed
    if keys[pygame.K_a]: player_x -= speed
    if keys[pygame.K_d]: player_x += speed
    """
}
features = {}

def extract_features(text):
    text = text.lower()
    found = []
    for feature, keywords in features.items():
        if any(k in text for k in keywords):
            found.append(feature)
    return found

def clarify(feature,features):
  if feature not in features:
    return "I don't have {feature} yet."
  return "I got you!"

def generate_code(task):
    task = task.lower().strip()

    # ---------------- IMPORT ----------------
    match = re.search(r"(import|get module|use)\s+(\w+)", task)
    if match:
        lib = match.group(2)
        return CODE_TEMPLATES["get_module"].format(library_name=lib)

    # ---------------- FUNCTION ----------------
    match = re.search(r"function\s+(\w+)\s+with\s+args?\s+(.+)", task)
    if match:
        name, args = match.groups()
        body = indent("print('running function')\nresult = None")
        return CODE_TEMPLATES["function"].format(
            func_name=name,
            args=args.replace(" and ", ", "),
            body=body,
            result="result"
        )

    # ---------------- LOOP ----------------
    match = re.search(r"loop\s+(\w+)\s+in\s+(.+)", task)
    if match:
        var, iterable = match.groups()
        body = indent("print(" + var + ")")
        return CODE_TEMPLATES["loop"].format(
            var=var,
            iterable=iterable,
            body=body
        )

    # ---------------- IF CHECK ----------------
    match = re.search(r"(\w+)\s*(==|<=|>=|!=|>|<)\s*(\w+)", task)
    if match:
        item1, op, item2 = match.groups()
        body = indent("print('Condition met fr')")
        return CODE_TEMPLATES["check"].format(
            item=item1,
            check_op=op,
            item2=item2,
            body=body
        )

    # ---------------- ASSIGNMENT ----------------
    match = re.search(r"set\s+(\w+)\s+to\s+(.+)", task)
    if match:
        var, val = match.groups()
        return CODE_TEMPLATES["assign"].format(var=var, value=val)

    # ---------------- PRINT ----------------
    match = re.search(r"print\s+(.+)", task)
    if match:
        target = match.group(1)
        return CODE_TEMPLATES["print"].format(target=target)

    # ---------------- MATH ----------------
    if any(op in task for op in ["+", "-", "*", "/"]):
        nums = re.findall(r"\d+", task)
        op = re.search(r"(\+|\-|\*|/)", task)
        if len(nums) >= 2 and op:
            expr = f"{nums[0]} {op.group(1)} {nums[1]}"
            return CODE_TEMPLATES["constant"].format(var="result", expr=expr) + "\nprint(result)"

    return f"I am still learning how to code: {task}"
