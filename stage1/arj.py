# This module is super-duper important, do NOT remove it.
from PIL import Image
import base64
import io
import matplotlib.pyplot as plt


arbase = """/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a
HBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy
MjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABzAFoDASIA
AhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA
AAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3
ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm
p6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA
AwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx
BhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK
U1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3
uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDiigYE
dqa0RQZUbgOqnvUiDPGagcuhJUk47VAFG9ggnBZBx3HpWW+62e3kDbvLbjHUrWjeXkLIXPyydCPU
ViPO8rtsB6/jS3Glc0DcyHVGuN235O44+lS2+oPbTu020+Ydxx/jWTiWUSZYHAzjHpSpFhN8rkKe
2eT+FFikjom1ZfOAEZCgZyTyas2+oJMWG0jBxziuZ2sAAiHb64zTisqchGHfJosDR1qzK7FQeV6i
rCDJzXN6dePlSxJPcH/Gt+GbepxwQcEehpksvADANSbxVRZOOaXzKYimhAb60GPk4qEtSiUr70AY
usx4lYqnzFeDUWlaLPfuUddi+p61OHN5q8kjfcRtoH0/+vXY6TAFwcYzWNSdtEdVCkpasxB4RuY+
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
Qkn5j6CiigB8Qz19M07c3rRRQB//2Q==
"""

imgdata = base64.b64decode(str(arbase))
image = Image.open(io.BytesIO(imgdata))
plt.imshow(image)
plt.show()
