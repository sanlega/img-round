# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    round.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/16 08:23:50 by slegaris          #+#    #+#              #
#    Updated: 2023/06/16 08:32:24 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
from PIL import Image, ImageDraw

def round_corners(image_path, output_path, radius):
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size

    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)

    draw.ellipse((0, 0, radius*2, radius*2), fill=255)  # top left
    draw.ellipse((width - radius*2, 0, width, radius*2), fill=255)  # top right
    draw.ellipse((0, height - radius*2, radius*2, height), fill=255)  # bottom left
    draw.ellipse((width - radius*2, height - radius*2, width, height), fill=255)  # bottom right
    draw.rectangle([radius, 0, width - radius, height], fill=255)  # top and bottom
    draw.rectangle([0, radius, width, height - radius], fill=255)  # left and right

    result = Image.new('RGBA', (width, height))
    result.paste(img, mask=mask)

    result.save(output_path, format="png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Round the corners of an image.')
    parser.add_argument('image_path', type=str, help='The path to the input image.')
    parser.add_argument('output_path', type=str, help='The path to save the output image.')
    parser.add_argument('radius', type=int, help='The radius for the rounded corners.')
    
    args = parser.parse_args()

    round_corners(args.image_path, args.output_path, args.radius)
