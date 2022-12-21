from IPython.core.display import display, HTML, Markdown
import json
import os.path
import csv
import ipywidgets as widgets
import datetime

class Announce:
    """error index, serves as an id on the csv file"""
    eindex = 0

    def __init__(self, etype, value):
        self.eindex = Announce.eindex
        Announce.eindex += 1
        self.etype = etype
        self.value = value
        self.feedbackRating = 0
        self.feedbackMSG = ""
        self.errorname = str(etype().__class__.__name__)
        with open("errorConfig.json", "r") as f:
            diction = json.load(f)
        exceptionClass = diction.get(self.errorname)
        prewrittenMessge = False
        
        if exceptionClass is None:
            self.print = False
        else:
            self.print = True
            for i in exceptionClass:
                key, items = list(i.items())[0]
                if (key in str(value)):
                    prewrittenMessge = True
            self.print = prewrittenMessge

        def writeRow(file):
            """saves errors to errorLog.csv"""
            fieldnames = ['index', 'errorType', 'errorMSG', 'feedbackRating', 'feedbackMSG', "Time"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({"index": self.eindex,
                            "errorType": self.errorname,
                            "errorMSG": str(self.value),
                            "feedbackRating": self.feedbackRating,
                            "feedbackMSG": self.feedbackMSG,
                            "Time": str(datetime.datetime.now())})

        if not os.path.isfile("errorLog.csv"):
            with open('errorLog.csv', 'w', newline='') as f:
                writeRow(f)
        else:
            if Announce.eindex == 1:
                with open("errorLog.csv", 'r') as f:
                    for row in csv.reader(f):
                        self.eindex = int(row[0])
                    self.eindex += 1
                    Announce.eindex = self.eindex + 1
            with open('errorLog.csv', 'a', newline='') as f:
                writeRow(f)
    
    def tips(self):
        etype = self.etype
        value = self.value
        with open("errorConfig.json", "r") as f:
            diction = json.load(f)
        exceptionClass = diction.get(self.errorname)
        if exceptionClass is not None:
            self.default()
            for i in exceptionClass:
                key, items = list(i.items())[0]
                if (key in str(value)):
                    c=1
                    for j in items.get("helptext"):

                        display(Markdown(str(c)+". "+j))
                        c += 1
    def data8(self):
        display(Markdown("The Data 8 Reference might be helpful to look over for examples and usage: [Data 8 Reference](http://data8.org/sp22/python-reference.html)"))
    def furtherTips(self):
        display(Markdown("If you are having more trouble please feel free to consult a staff member \
                        \n or see the error message below "))
    def print(self, i):
        display(Markdown)
    def title(self):
        display(Markdown("## **Uh-o it seems we have an error!**"))
    def default(self):
        display(Markdown("It seems we have a "+self.errorname+ ". " +self.errorname+ "s are usually because of:"))
    def feedback(self):
        def overwriteRow():
            """rewrites the feedbackRating & feedbackMSG columns on errorLog.csv"""
            with open("errorLog.csv", 'r') as f:
                reader = csv.reader(f, delimiter=',')
                lines = []
                for line in reader:
                    if line[0] == str(self.eindex):
                        line[3] = self.feedbackRating
                        line[4] = self.feedbackMSG
                    lines.append(line)
            with open("errorLog.csv", 'w', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerows(lines)

        """create & label a dropdown menu"""
        dropdown_label = widgets.Label(value="Was the message you saw useful?")
        dropdown = widgets.Dropdown(options=[('', 0),
                                             ('Extremely useful', 5),
                                             ('Very useful', 4),
                                             ('Somewhat useful', 3),
                                             ('Slightly useful', 2),
                                             ('Not at all useful', 1)],
                                    value=0)
        def handle_slider_change(change):
            """on change: rewrites the feedbackRating in the CSV"""
            self.feedbackRating = dropdown.value
            overwriteRow()
        dropdown.observe(handle_slider_change)

        """create & label a textbox"""
        textbox_label = widgets.Label(value="Any other feedback?")
        textbox = widgets.Text(value="",
                               placeholder="Press enter to submit.",
                               layout=widgets.Layout(width='50%', margin='0px 8px 0px 0px', padding='0px'))
        def submit_text(t):
            """on textbox submit: remove other fields and replace with a thank you message"""
            self.feedbackMSG = t.value
            accordion.children = [widgets.Label(value="Thank you for your feedback!")]
            overwriteRow()
        textbox.on_submit(submit_text)

        """create a submit button for the textbox"""
        submit_button = widgets.Button(description="Submit",
                                       layout=widgets.Layout(width='10%', min_width='80px'))
        def on_btn_click(b):
            """on button click: submits textbox and replaces other fields with a thank you message"""
            submit_text(textbox)
        submit_button.on_click(on_btn_click)
        
        """bundle together widgets for a cleaner output"""
        dropdownBox = widgets.VBox([dropdown_label, dropdown])
        submitBox = widgets.HBox([textbox, submit_button])
        submitBox.layout.align_items = 'center'
        textboxBox = widgets.VBox([textbox_label, submitBox])
        output = widgets.VBox([dropdownBox, textboxBox])
        accordion = widgets.Accordion([output])
        accordion.set_title(0, '  Feedback Form')

        display(accordion)

def test_exception(self, etype, value, tb, tb_offset=None):
    try:
        announce = Announce(etype, value)
        if announce.print:
            announce.title()
            announce.tips()
            announce.data8()
            announce.furtherTips()
            announce.feedback()
        self.showtraceback((etype, value, tb), tb_offset=tb_offset)
    except:
        self.showtraceback((etype, value, tb), tb_offset=tb_offset)
    
get_ipython().set_custom_exc((Exception,), test_exception)
