# There's probably an easier way to do this.

### But whatever.

This thing helps you randomly choose emails from a list of emails that you copy from Outlook. You need Python to run this (if you did ICS3U, you'll have it).

## Steps

1. Download this repository (Git clone or Download ZIP). ![image-20191107223618028](C:\Users\2021158\OneDrive - Appleby College\S1\Math\GlobalIssue\image-20191107223618028.png)

2. Go to Outlook and select all of the groups you want in your population. // TODO add photo

3. Expand these, select all (Ctrl + A), and copy // TODO add photo

4. In the repository, create a new text file called text.txt and paste whatever you have on clipboard in there.

5. Open format.py in Notepad and change SAMPLESIZE variable to however many random addresses you need. ![image-20191107225227884](C:\Users\2021158\OneDrive - Appleby College\S1\Math\GlobalIssue\image-20191107225227884.png) 

6. Open a command line an run in the repository directory:

   ```
   python format.py
   ```

7. Open the newly create results.txt and copy all contents. ![image-20191107225714301](C:\Users\2021158\OneDrive - Appleby College\S1\Math\GlobalIssue\image-20191107225714301.png)
8. Paste this into the recipients for email you want to send and click "Check Names". ![image-20191107225631471](C:\Users\2021158\OneDrive - Appleby College\S1\Math\GlobalIssue\image-20191107225631471.png)
9. Your recipients are set!

## Problems?

Create an issue and I'll try to fix. 