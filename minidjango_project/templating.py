import os

def render_template(template_name, context):
    """
    Renders a template with the given context.
    - template_name: The filename of the template (e.g., 'home.html').
    - context: A dictionary of data to inject into the template.
    """
    # Build the full path to the template file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, 'templates', template_name)

    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # Replace placeholders like {{ key }} with values from the context
        for key, value in context.items():
            placeholder = f"{{{{ {key} }}}}"  # Creates the string "{{ key }}"
            template_content = template_content.replace(placeholder, str(value))
        
        return template_content

    except FileNotFoundError:
        return "<h1>Error: Template not found</h1>"