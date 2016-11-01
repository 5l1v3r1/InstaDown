# InstaDown v2

*Commandline Instagram Downloader written by Python using Instagram API*

---
**DISCLAIMER:**

This code is shared for informational purposes only. Use of Instagram is governed by the company's Terms of Use (http://instagram.com/legal/terms/). Any user content posted to Instagram is governed by the Privacy Policy (http://instagram.com/legal/privacy/). 

---

###Read before use:
You should have developer token id for Instagram. If you're using your own application, you can experience some problems caused by Instagram's new api restrictions. I won't support that situations.
You can use [here](http://services.chrisriversdesign.com/instagram-token/) for taking unproblematic one.

###Usage
```
usage: main.py [-h] -u [username] [-l [path]] {[--list] [-o [file]]}
```

```
***                   *             *****
 *                    *              *   *
 *                    *              *   *
 *   * ***    ****   ****    ****    *   *   ****   *     *  * ***
 *   **   *  *    *   *          *   *   *  *    *  *     *  **   *
 *   *    *   **      *      *****   *   *  *    *  *  *  *  *    *
 *   *    *     **    *     *    *   *   *  *    *  *  *  *  *    *
 *   *    *  *    *   *  *  *   **   *   *  *    *  *  *  *  *    *
***  *    *   ****     **    *** *  *****    ****    ** **   *    * v2


[0.00%] Downloading: #1
[7.14%] Downloading: #2
[14.29%] Downloading: #3
[21.43%] Downloading: #4
[28.57%] Downloading: #5
[35.71%] Downloading: #6
[42.86%] Downloading: #7
[50.00%] Downloading: #8
[57.14%] Downloading: #9
[64.29%] Downloading: #10
[71.43%] Downloading: #11
[78.57%] Downloading: #12
[85.71%] Downloading: #13
[92.86%] Downloading: #14
[100.00%] Downloading: #15

```

###Changelog
**02.11.2016:**
- New feature: Listing photo URLs. You can print or save on file it. 
- More modular functions in `instadown.py`. You can use it as library in your projects. 
- Better error and exception handling. 
- Better help menu with colors.
- Some bugfix and performance improvements. (Approx. download 100 photos/min. in my tests.)

**Warnings** 
 
 - If download directory doesn't exist before run, it creates one.
 - If url list file doesn't exist before run, it creates one.
 - I couldn't test it on Windows and Mac but it must work.


