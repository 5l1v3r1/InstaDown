# coding=utf-8
__author__ = 'kandalf'

import argparse
from instadown import *

print ''' \033[94m

***                   *             *****
 *                    *              *   *
 *                    *              *   *
 *   * ***    ****   ****    ****    *   *   ****   *     *  * ***
 *   **   *  *    *   *          *   *   *  *    *  *     *  **   *
 *   *    *   **      *      *****   *   *  *    *  *  *  *  *    *
 *   *    *     **    *     *    *   *   *  *    *  *  *  *  *    *
 *   *    *  *    *   *  *  *   **   *   *  *    *  *  *  *  *    *
***  *    *   ****     **    *** *  *****    ****    ** **   *    *

\033[0m'''

parser = argparse.ArgumentParser(description='Download photos of spesific user.')
parser.add_argument('-u', nargs='?', help='Username')
parser.add_argument('-l', nargs='?', help='Download path. If directory doesn\'t exist, create it.')
args = parser.parse_args()

Instagram = InstaDown()
Instagram.getID(args.u)
Instagram.getMediaCount()
Instagram.getMedia(args.l)