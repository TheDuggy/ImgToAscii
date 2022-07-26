# Copyright 2022 Georg Kollegger (CoderTheDuggy/TheDuggy)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import PIL.Image
import os
import numpy
import sys
import colorama


def logOK(msg, stayInLine):
    print('\033[92m[+] ' + msg + '\033[0m', end='' if stayInLine else '\n')


def logFATAL(msg, inNewLine):
    print(('\n' if inNewLine else '') + '\033[91m[-] ' + msg + '\033[0m')


def logWARNING(msg):
    print('\033[93m[!] ' + msg + '\033[0m')


def getColorChar(rgbAverage):
    if 0 <= rgbAverage < 17:
        return '.'
    elif 17 <= rgbAverage < 34:
        return '_'
    elif 34 <= rgbAverage < 51:
        return '*'
    elif 51 <= rgbAverage < 68:
        return ':'
    elif 68 <= rgbAverage < 85:
        return '-'
    elif 85 <= rgbAverage < 102:
        return '~'
    elif 102 <= rgbAverage < 119:
        return '>'
    elif 119 <= rgbAverage < 136:
        return '/'
    elif 136 <= rgbAverage < 153:
        return '!'
    elif 153 <= rgbAverage < 170:
        return '|'
    elif 170 <= rgbAverage < 187:
        return '§'
    elif 187 <= rgbAverage < 204:
        return '&'
    elif 204 <= rgbAverage < 221:
        return '$'
    elif 221 <= rgbAverage < 238:
        return '%'
    elif 238 <= rgbAverage <= 255:
        return '#'


def main():
    background = '\u001b[41m'
    background2 = '\u001b[104m'
    blue = '\033[34m'
    red = '\033[31m'
    reset = '\033[0m'

    line1 = ' ____________                               _                   _____________'
    line2 = '|_' + background + '             ' + reset + '                          __| ' + background + '  ' + reset + '                ' + '| ' + background2 + '              ' + reset
    line3 = '     | ' + background + '   ' + reset + '                              |_' + background + '        ' + reset + '             ' + '| ' + background2 + '   ' + reset + '      | ' + background2 + '   ' + reset
    line4 = '     | ' + background + '   ' + reset + '      ___________   _______      | ' + background + '  ' + reset + '   _______' + reset + '      ' + '| ' + background2 + '   ' + reset + '      | ' + background2 + '   ' + reset + ' _______   _______   _   _'
    line5 = '     | ' + background + '   ' + reset + '     | ' + background + '            ' + reset + '| ' + background + '        ' + reset + '    | ' + background + '  ' + reset + '  | ' + background + '        ' + reset + '    ' + '| ' + background2 + '   ' + reset + '______| ' + background2 + '   ' + reset + '| ' + background2 + '        ' + reset + '| ' + background2 + '        ' + reset + '|_' + background2 + '  ' + reset + '|_' + background2 + '  ' + reset
    line6 = '     | ' + background + '   ' + reset + '     | ' + background + '  ' + reset + ' | ' + background + '  ' + reset + ' | ' + background + '  ' + reset + '| ' + background + '  ' + reset + '  | ' + background + '  ' + reset + '    | ' + background + '  ' + reset + '  | ' + background + '  ' + reset + '  | ' + background + '  ' + reset + '    ' + '| ' + background2 + '              ' + reset + '| ' + background2 + '  ' + reset + '____  | ' + background2 + '  ' + reset + '       _   _'
    line7 = '     | ' + background + '   ' + reset + '     | ' + background + '  ' + reset + ' | ' + background + '  ' + reset + ' | ' + background + '  ' + reset + '| ' + background + '  ' + reset + '  | ' + background + '  ' + reset + '    | ' + background + '  ' + reset + '  | ' + background + '  ' + reset + '  | ' + background + '  ' + reset + '    ' + '| ' + background2 + '   ' + reset + '      | ' + background2 + '   ' + reset + '|_' + background2 + '        ' + reset + '| ' + background2 + '  ' + reset + '      | ' + background2 + '  ' + reset + '| ' + background2 + '  ' + reset
    line8 = ' ____| ' + background + '   ' + reset + '___  | ' + background + '  ' + reset + ' | ' + background + '  ' + reset + ' | ' + background + '  ' + reset + '| ' + background + '  ' + reset + '__| ' + background + '  ' + reset + '    | ' + background + '  ' + reset + '  | ' + background + '  ' + reset + '__| ' + background + '  ' + reset + '    ' + '| ' + background2 + '   ' + reset + '      | ' + background2 + '   ' + reset + ' _____| ' + background2 + '  ' + reset + '| ' + background2 + '  ' + reset + '____  | ' + background2 + '  ' + reset + '| ' + background2 + '  ' + reset
    line9 = '|_' + background + '             ' + reset + '|_' + background + '  ' + reset + ' |_' + background + '  ' + reset + ' |_' + background + '  ' + reset + '|_' + background + '        ' + reset + '    |_' + background + '  ' + reset + '  |_' + background + '        ' + reset + '    ' + '|_' + background2 + '   ' + reset + '      |_' + background2 + '   ' + reset + '|_' + background2 + '        ' + reset + '|_' + background2 + '        ' + reset + '|_' + background2 + '  ' + reset + '|_' + background2 + '  ' + reset
    line10 = '                                   | ' + background + '  ' + reset
    line11 = '                              _____| ' + background + '  ' + reset
    line12 = '                             |_' + background + '        ' + reset

    print(
        line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line7 + '\n' + line8 + '\n' + line9 + '\n' + line10 + '\n' + line11 + '\n' + line12 + '\n' + ' ' * 56 + red + 'v1.0' + '\n' + ' ' * 37 + blue + '(C) Georg Kollegger (CoderTheDuggy/TheDuggy)\n' + reset)

    customPath = ''
    createFile = True
    if len(sys.argv) > 1:
        if sys.argv[1] == '--no-file':
            createFile = False
            logWARNING('Save result to file has been disabled with arg --no-file!')
        elif sys.argv[1].split('=', 1)[0] == '--custom-output-file':
            if os.path.exists(sys.argv[1].split('=', 1)[1]) and os.path.isdir(sys.argv[1].split('=', 1)[1]):
                customPath = sys.argv[1].split('=', 1)[1] + '/'
                logWARNING('Custom output-dir was set to ' + customPath + '!')
            else:

                logWARNING('Custom output-dir was set to ' + sys.argv[1].split('=', 1)[1] + ' but doesn\'t exist or isn\'t a directory! Using default ./ instead!')
        else:
            logWARNING('The command line argument ' + sys.argv[1] + ' is unknown and skipped!' + (
                '(Along with ' + str(len(sys.argv) - 2) + ' other argument(s)!' if len(sys.argv) > 3 else ''))

    logOK('Please enter the path to your image: ', True)
    filePath = input('')
    if os.path.exists(filePath):
        if os.path.isfile(filePath):
            image = PIL.Image.open(filePath)
            logOK('Enter width (or nothing/0 to calculate it from height): ', True)
            width = input('')
            width = width if width else 0

            logOK('Enter height (or nothing/0 to calculate it from width): ', True)
            height = input('')
            height = height if height else 0

            if not str(width).isnumeric():
                logFATAL('The width (' + width + ') is not numeric!', False)
                exit(0)
            if not str(height).isnumeric():
                logFATAL('The height (' + height + ') is not numeric!', False)
                exit(0)

            height = int(height)
            width = int(width)

            resultHeight = height
            resultWidth = width
            if height == 0 and width != 0:
                resultHeight = round(
                    image.height * (image.width / width) if width > image.width else image.height / (
                            image.width / width))
            elif height != 0 and width == 0:
                resultWidth = round(image.width * (image.height / height) if height > image.height else image.width / (
                        image.height / height))
            elif height == 0 and width == 0:
                resultWidth = image.width
                resultHeight = image.height

            logOK('Enter a offset for the text (or nothing to calculate the default offset): ', True)
            offset = input('')
            if offset:
                if not str(offset).isnumeric():
                    if not offset == 'disabled':
                        logFATAL('The offset must be numeric!', False)
                        exit(0)
                else:
                    offset = ' ' * int(offset)

            resizedImage = image.resize((resultWidth, resultHeight))

            if not offset:
                if 100 <= resizedImage.height <= 200 or 100 <= resizedImage.width <= 200:
                    offset = ' '
                elif resizedImage.height > 200 or resizedImage.width > 200:
                    offset = ' ' * round(resizedImage.height / 2 / 100)
            if offset == 'disabled':
                offset = ''

            pixels = resizedImage.load()
            resultFileName = 'result-' + os.path.basename(filePath) + '.txt'
            file = open(('./' if customPath == '' else customPath) + resultFileName, 'wb')
            logOK('Creating chars of image ' + file.name + 'with height=' + str(resizedImage.height) + ', width=' + str(resizedImage.width) + ' and ' + ('no offset!' if offset == '' else ' offset=' + offset + '!'), False)
            for y in range(0, resizedImage.height):
                for x in range(0, resizedImage.width):
                    rgb = numpy.array(pixels[x, y])
                    rgbAverage = round((rgb[0] + rgb[1] + rgb[2]) / 3)
                    colorChar = getColorChar(rgbAverage)
                    print(colorChar + offset, end='')
                    if createFile:
                        file.write((colorChar + offset).encode('utf8'))
                print('')
                if createFile:
                    file.write('\n'.encode('utf8'))

            file.close()
            logOK('Saved result to file ' + resultFileName + '!', False)
        else:
            logFATAL('File ' + filePath + ' isn\'t a file!', False)
    else:
        logFATAL('File ' + filePath + ' doesn\'t exist!', False)


colorama.init()
try:
    main()
except KeyboardInterrupt:
    logFATAL('Quitting...', True)
