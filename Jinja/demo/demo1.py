from jinja2 import Template

def demo_a():
    t = Template("Hello {{ something }}!")
    print(t.render(something="World"))

def demo_b():
    t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
    print(t.render())


if __name__ == "__main__":
    demos  = [ func for (name, func) in locals().items()  if name.startswith('demo_') and callable(func) ]
    for demo in demos:
        print(f"{'*'*12}\n** {demo.__name__} ::\n{'*'*12}")
        demo()
    print("== Done\n")
