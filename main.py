from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask("DSA Hub")

# Setting multiple routes
@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():
    return render_template("index.html")

@app.route("/pygments-demo/")
def pygmentsDemo():
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import HtmlFormatter
    from pygments.styles import get_style_by_name

    f = open("main.py", "r")
    code = ''.join(f.readlines())
    f.close()

    lexer = get_lexer_by_name("python", stripall=True)
    formatter = HtmlFormatter(linenos=True, full=True)

    return (highlight(code, lexer, formatter))

@app.route("/demo/")
def demo():
    page_data = dict()
    page_data['title'] = "Demo Algorithm"
    page_data['heading'] = page_data['title']
    return render_template('content_layout.html', page_data = page_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1306, debug=True)
