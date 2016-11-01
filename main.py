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
***  *    *   ****     **    *** *  *****    ****    ** **   *    * v2

\033[0m'''

parser = argparse.ArgumentParser(description=' \033[94m Downloads the spesific user\'s Instagram photos. \033[0m')
parser.add_argument('-u', nargs='?', help='\033[94m Username\033[0m', required=True,metavar='username')
parser.add_argument('-l', nargs='?', help='\033[94m Download path. If directory doesn\'t exist, it creates one. \033[0m',metavar="path")
parser.add_argument('--list', dest='nodownload', action='store_true', help='\033[94m No download, just list photo urls. \033[0m')
parser.add_argument('-o', nargs='?', help='\033[94m Path of output file for url list. It\'s useful you want to use download manager.\033[0m\033[93m Ex: /home/kandalf/url.txt \033[0m',metavar="file",type=argparse.FileType('w'))
parser.set_defaults(nodownload=False)
args = parser.parse_args()

Instagram = InstaDown('<add_token_here>') # Write Instagram developer token id here. You can get your own at http://services.chrisriversdesign.com/instagram-token/ 
userid = Instagram.getUserID(args.u)
count = Instagram.getMediaCount(userid)

if args.nodownload:
	
	downloadList = Instagram.getMedia(userId=userid, path="", mediaCount=count, download=False)
	
	if args.l != None:
		parser.error('you can\'t use argument -l with --list')
	if args.l !=None and args.o != None:
		parser.error('you can\'t use argument -l with -o')
	
	if args.o == None:
		for url in downloadList:
			print link, '\n'
	else:
		for url in downloadList:
			args.o.write(url + '\n')

else:
	
	if args.o != None and args.l == None:
		parser.error('you can\'t use argument -o without --list')
	if args.l == None:
		parser.error('argument -l is required')
	if args.o != None:
		parser.error('you can\'t use argument -o without --list')
	
	Instagram.getMedia(userId=userid, path=args.l, mediaCount=count, download=True)