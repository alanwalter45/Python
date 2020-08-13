def createElement(element, **attrs):
    attrs = ' '.join([f'{k}="{v}"' for k, v in attrs.items()])
    return f"<{element} {attrs}>"


print(createElement('div', height="500px", width="200px", background="orange"))
