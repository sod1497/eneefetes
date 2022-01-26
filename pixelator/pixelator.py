from pathlib import Path

import numpy as np
from svglib import svglib
from reportlab.graphics import renderPM
import cv2

BASE_PATH = Path(__file__).resolve().parent


class Pixelator:

    def __init__(self):
        pass

    @classmethod
    def pixelate_svg(cls, filepath: Path):
        filepath_png = BASE_PATH.joinpath('..', 'output', 'result.png')

        renderPM.drawToFile(svglib.svg2rlg(filepath), filepath_png, fmt="PNG")

        palette = 5

        # img_array = np.fromfile(filepath_png, np.uint8)
        # with open(filepath_png, "rb") as file:
        #     img_array = np.asarray(bytearray(file.read()), dtype=np.uint8)
        # input = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

        image = cv2.imread('./output/result.png', cv2.IMREAD_COLOR)

        # colorReduce()
        quantized = image // palette * palette + palette // 2
        quantized_2 = quantize(image, palette)

        cv2.imwrite('./output/result_palette.png', quantized_2)


def quantize(image, palette):
    # Color y su frecuencia
    colors = {}
    for c in image:
        for r in c:
            if str(r.tolist()) in colors:
                colors[str(r.tolist())] += 1
            else:
                colors[str(r.tolist())] = 1

    # Tomar tantos colores como indique palette
    colors = {k: v for k, v in sorted(colors.items(), key=lambda item: item[1], reverse=True)}
    color_palette = list(colors.keys())[:palette]  # TODO: contemplar que palette sea más grande que colors
    color_palette = [[int(y) for y in x.replace('[', '').replace(']', '').split(', ')] for x in color_palette]

    # Aproximar colores al mas cercano
    result = []
    for c in image:
        aux_c = []
        for r in c:
            if r.tolist() in color_palette:
                aux_c.append(r)
            else:
                # Aproximar
                distances = {str(x): np.linalg.norm(r - np.array(x)) for x in color_palette}
                min_distance_color = min(distances, key=distances.get)
                aux_c.append(list(filter(lambda x: str(x) == min_distance_color, color_palette))[0])

        result.append(aux_c)

    return np.array(result)

