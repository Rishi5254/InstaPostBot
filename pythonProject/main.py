from niceposter import Create
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
import shutil


def get_clean_data(data):

    no_of_lines = 14

    # content = ""
    # for i in range(no_of_lines):
    #     content += input()+"\n"

    con_list = data.split()
    print(f"list ::: {con_list}")
    output = []
    company_name = ""
    role = ""
    comany_name_index = 0
    location = ""
    symbols_list = []
    qualification = ""
    work_experience = ""
    ctc = ""
    apply_link = ""
    print(con_list)
    # finding off index
    for index, string in enumerate(con_list):
        if 'Off' in string:
            comany_name_index = index
        if 'On' in string:
            comany_name_index = index
        if ':' in string:
            symbols_list.append(index)
    # Comany name output.
    for index, item in enumerate(con_list[0:comany_name_index]):
        company_name += item
        company_name += " "
    # Role output .
    hit = 0
    for index, string in enumerate(con_list):
        if string[0] == "*" and string[-1] == "*":
            role += string[1:-1]
            break
        if string[0] == "*":
            hit = 1
            role += string[1:]
            role += " "
            continue
        if string[-1] == "*":
            role += string[0:-1]
            role += " "
            hit = 0
            continue
        if hit == 1:
            role += string
            role += " "
    # for index, word in enumerate(con_list):
    #     if word == "Location" or word == "Location:" :
    # location output
    for i in range(symbols_list[0] + 1, symbols_list[1]):
        if con_list[i] != 'Qualification' and con_list[i] != 'Qualification:':
            location += con_list[i]
            location += " "
    for i in range(symbols_list[1] + 1, symbols_list[2]):
        if con_list[i] != 'Work' and con_list[i] != 'Experience:' and con_list[i] != 'Experience':
            qualification += con_list[i]
            qualification += " "

    for i in range(symbols_list[2] + 1, symbols_list[3]):
        if con_list[i] != 'CTC' and con_list[i] != 'CTC:':
            work_experience += con_list[i]
            work_experience += " "

    for i in range(symbols_list[3] + 1, symbols_list[4]):
        if con_list[i] != 'Apply' and con_list[i] != 'Link' and con_list[i] != 'Link:':
            ctc += con_list[i]
            ctc += " "

    for i in range(symbols_list[4] + 1, symbols_list[5] + 1):
        apply_link += con_list[i]
        apply_link += " "


    im = Create.Poster()

    im.add_image('image.png', position='cc', scale='cover')

    new_company_name = ""
    for index, word in enumerate(company_name):
        if index > 17 :
            if word == " ":
                break
            else:
                new_company_name += word
        else:
            if word == " ":
                new_company_name += ""
            else:
                new_company_name += word


    im.text(new_company_name, position=(194, 65), color='#000000', text_size=21)

    new_role = ""
    for index, word in enumerate(role):
        if index > 25 :
            if word == " ":
                break
            else:
                new_role += word
        else:
            if word == " ":
                new_role += ""
            else:
                new_role += word

    im.text(new_role, position=(86, 113), color='#000000', text_size=21,)

    new_location = ""
    for index, word in enumerate(location):
        if index > 24 :
            new_location = "PanIndia"
            break
        else:
            if word == " ":
                new_location += ""
            else:
                new_location += word



    im.text(new_location, position=(133, 161), color='#000000', text_size=22,)

    new_qualification = ""
    for index, word in enumerate(qualification):
        if index > 22 :
            new_qualification = "Any Graduation"
            break
        else:
            if word == " ":
                new_qualification += ""
            else:
                new_qualification += word


    im.text(new_qualification, position=(182, 212), color='#000000', text_size=22,)

    new_work_exp = ""
    for index, word in enumerate(work_experience):
        if index > 19:
            new_work_exp = "Fresher"
            break
        else:
            if word == " ":
                new_work_exp += ""
            else:
                new_work_exp += word


    im.text(new_work_exp, position=(214, 267), color='#000000', text_size=22,)

    new_ctc = ""
    for index, word in enumerate(ctc):
        if index > 29:
            new_ctc = "Refer Link for CTC info"
            break
        else:
            if word == " ":
                new_ctc += ""
            else:
                new_ctc += word

    im.text(new_ctc, position=(77, 316), color='#000000', text_size=22,)

    im.text(apply_link, position=(147, 363), color='#000000', text_size=22,)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretcode'
Bootstrap(app)

class AddForm(FlaskForm):
    title = TextAreaField("Enter Text", validators=[DataRequired()])
    submit = SubmitField("Get Post")


@app.route('/homepage')
def get_image():
    return render_template("homepage.html")


@app.route("/",  methods=['GET', 'POST'])
def homepage():
    form = AddForm()
    if form.validate_on_submit():
        data = form.title.data
        print(data)
        get_clean_data(data)
        # Path of the image file to be copied
        src = 'img.png'
        # Path of the destination folder
        dst = 'static/images/'
        # Copy the image file from source to destination
        shutil.copy(src, dst)
        return redirect(url_for('get_image'))
    return render_template("index.html", form=form)




if __name__ == "__main__":
    app.run(debug=True)




