# 🙌 Awesome FastHTML 👏
Awesome and Best FastHTML Resources For Developers. Create a PR to contribute to this repo.

## Examples
**A Simple Video Player in Pure Python**

```python
from fasthtml.common import *

# Create app and router instances
app, rt = fast_app()

# Define a route decorator
@rt('/')  # Define a route for the root path or home route
def get():
    return Div(
        H1('Up and running with FastHTML!'),
        Video(
            Source(src='movie.mp4', type='video/mp4'),
            Source(src='movie.ogg', type='video/ogg'),
            'Your browser does not support the video tag.',
            width=460,
            height=380,
            controls=True,
            style='''
                border: 6px solid #005fff; 
                border-radius: 32px; 
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            '''
        ),
        Style(
            '''
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                text-align: center;
                color: #005fff;
            }
            '''
        ),
    )

serve()
```

## Core Technologies 
- [FastHTML Website](https://www.fastht.ml/)
- [HTMX](https://htmx.org/)
- [Python](https://www.python.org/)

## Tools 
- [HTML to FastTag (FT)](https://h2x.answer.ai/)
- [Answer AI's HTML to Markdown](https://web2md.answer.ai/)

## Styling a FastHTML App
- [Pico✨](https://picocss.com/)
- [Tailwind](https://tailwindcss.com/)
- [daisyUI](https://daisyui.com/)

## GitHub
- [Oficial FastHTML Docs](https://github.com/AnswerDotAI/fasthtml)
- [FastHTML Gallery](https://github.com/Isaac-Flath/FastHTML-Gallery)

## YouTube Videos
- [Fireship July 2024 Code Report: FastHTML Framework](https://youtu.be/l0e9i8zXcIs?si=Vz45eCEExM4DeRcF)
- [Getting Started With FastHTML](https://youtu.be/Auqrm7WFc0I?si=2TnF14KzuT0xD6y5)
- [FastHTML - The Fastest Way to Create an HTML App With Python](https://youtu.be/7OhBgkFtwFU?si=svG-_FNMD2M-NXYn)
- [Exploring FastHTML](https://youtu.be/4En57Zw6gU4?si=iVbgDEtcD9DVg56k)

## Articles
- [FastHTML: Everything You Need to Know](https://daily.dev/blog/fasthtml-everything-you-need-to-know-about-this-modern-web-framework-in-pure-python)
- [Creating Custom FastHTML Tags](https://isaac-flath.github.io/website/posts/boots/FasthtmlTutorial.html)
- [Python Framework that Changes Everything](https://medium.com/@hhartleyjs/this-new-python-web-framework-changes-everything-b667db75f6fd)

## Social
[Discord Community](https://discord.gg/qcXvcxMhdP)

## News
- [Product Hunt](https://www.producthunt.com/posts/fastht-ml)
- [Hacker News](https://news.ycombinator.com/item?id=41104305)
- [Reddit](https://www.reddit.com/r/Python/comments/1eghskf/jeremy_howard_cofounder_of_fastai_released/)
