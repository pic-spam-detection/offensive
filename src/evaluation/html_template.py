"""Generate an HTML report with evaluation metrics and visualizations"""

HTML_TEMPLATE_START = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Evaluation of Spam Email Generation</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
      }
      .container {
        width: 80%;
        margin: auto;
        padding: 20px;
        background: white;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
      h1, h2 {
        text-align: center;
        color: #333;
      }
      p {
        line-height: 1.6;
        color: #555;
      }
      img {
        height: 100%;
        max-height: 300px;
        box-shadow: 0 0 15px gray;
        border-radius: 5px;
        transition: transform 0.25s ease;
        cursor: zoom-in;
      }
      img.zoomed {
        cursor: zoom-out;
      }
      .images-container {
        display: flex;
        justify-items: center;
        gap: 15px;
        justify-content: center;
        align-items: center;
      }
      .image-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Evaluation of Spam Email Generation</h1>
    </header>
"""

HTML_TEMPLATE_END = """
    <script>
      document.querySelectorAll("img").forEach((i) => {
        i.addEventListener("click", (evt) => {
          if (i.classList.contains("zoomed")) i.style.transform = "";
          else {
            const myScale = 700 / i.clientWidth;
            i.style.transform = `scale(${myScale})`;
          }
          i.classList.toggle("zoomed");
        });
      });
    </script>
  </body>
</html>
"""


def write_template(data, filepath):
    result = HTML_TEMPLATE_START + '<div class="container">'
    for model, plots in data.items():
        result += f"<h2>{model}</h2>"
        result += '<div class="images-container">'

        for metric, plot in plots.items():
            result += f"""
            <div class="image-wrapper">
                <img src="{plot}" />
                <p>{metric}</p>
            </div>
        """
    result += "</div></div>"
    result += HTML_TEMPLATE_END

    with open(filepath, "w") as file:
        file.write(result)
