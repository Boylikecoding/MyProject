import streamlit as st
import json
from PIL import Image
from streamlit_lottie import st_lottie

#---page set up---
st.set_page_config(page_title = "Streamlit turtorial", page_icon=":computer", layout="wide")

#---multi page---
st.sidebar.success('For more info')

#---load local json---
def localjson( filepath = str ):
    with open(filepath, 'r') as f:
        return json.load(f)
    
#---asset---
intall_streamlit = Image.open("picture/install_streamlit.PNG")
create_project = Image.open("picture/create_project.PNG")
create_file = Image.open("picture/create_file.PNG")
import_streamlit = Image.open("picture/import_streamlit.PNG")
Run_streamlit = Image.open("picture/Run_streamlit.PNG")
ex_page = Image.open("picture/ex_page.PNG")
column1 = Image.open("picture/column1.PNG")
column2 = Image.open("picture/column2.PNG")
column_use = Image.open("picture/column_use.PNG")
ex_pic1 = Image.open("picture/ex_pic1.PNG")
ex_pic2 = Image.open("picture/ex_pic2.PNG")
ex_pic3 = Image.open("picture/ex_pic3.PNG")
download_json = Image.open("picture/download_json.PNG")
json_dir = Image.open("picture/json_dir.PNG")
header_pic = localjson("lottie/coding-slide.json")
bye_pic = localjson("lottie/green-bye.json")


#---header---
with st.container():
    st.markdown('''<p style="text-align: center;
      font-size: 50px;" ><b>Streamlit turtorial for beginner</b></p>''',unsafe_allow_html=True)
    st_lottie(header_pic, height=500)
    st.markdown('<p style=" text-align: center; font-size: 30px;">This turtorial will teach you how to create a simple webpage form the scarth by using Streamlit framwork and some necessary tools for python.</p>',unsafe_allow_html=True)

#---turtorial1---
with st.container():
    st.write("---")
    st.header("1. Install streamlit")
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write("- By open window command prompt type down then press enter :")
        st.code('pip install streamlit', language='C')
    with right_colmun:
        st.image(intall_streamlit)
#---turtorial1.1---
with st.container():
    st.write("---")
    st.subheader("1.1. import streamlit")
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.subheader("- Now create a directoty for your project")
        st.write("- for example : I have create the project folder on my desktop")
    with right_colmun:
        st.image(create_project)
#---turtorial1.2---
with st.container():
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.subheader("- Create a directoty for your project")
        st.write("- for example : I use Visual studio code to open a directoty I've just created and create a file name 'index.py'")
    with right_colmun:
        st.image(create_file)
#---turtorial1.3---
with st.container():
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.subheader("- Import streamlit to your prject")
        st.write("- By using the follwing syntax :")
        st.code('import streamlit as st')
    with right_colmun:
        st.image(import_streamlit)
#---turtorial1.2---
with st.container():
    st.write("###")
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.subheader("1.2. Run streamlit")
        st.write("- By opening the command promt and access the root directory of your project then use the follwing syntax :")
        st.code('streamlit run "your_file_name.py"')
        st.write("If everything correct your webpage will open automatically on your browser.")
    with right_colmun:
        st.write('<u>example</u> : I run streamtlit from my project root directory.',unsafe_allow_html=True)
        st.image(Run_streamlit)

#---turtorial2---
with st.container():
    st.write("---")
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.header("2. Set up web page")
        st.subheader("- Set up a web page by using the following syntax :")
        st.code('st.set_page_config(page_title = " ", page_icon=" ", layout=" ")')
        st.write('- you can set "page_title" as you like.')
        st.write('- for "page_icon" you can use emoji from this [www.webfx.com>](https://www.webfx.com/tools/emoji-cheat-sheet/)')
        st.write('- for "layout" you can choose between "wide" and "Center".')
    with right_colmun:
        st.image(ex_page)

#---turtorial3---
with st.container():
    st.write("---")
    st.header("3. header, subheader, paragraph and column")
    left_column,middle_column, right_colmun = st.columns(3)
    with left_column:
        st.subheader("3.1. Create header by using the following syntax :")
        st.code('st.header(" ")')
    with middle_column:
        st.subheader("3.2. Create subheader by using the following syntax :")
        st.code('st.subheader(" ")')
    with right_colmun:
        st.subheader("3.3. Create paragraph by using the following syntax :")
        st.code('st.write(" ")')
#---turtorial3.1---
with st.container():
    st.subheader("3.4. Create column by using the following syntax :")
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('''- The following syntax will create two column
                 split evenly between each other on the current container, you can add more column
                if you want. ''')
        st.code('column1, colmun2 = st.columns(2)')
    with right_colmun:
        st.image(column1)
with st.container():
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('''- You can also customize the space of your column for examlpe :
                    making the first column bigger than the second column with the following syntax:''')
        st.code('column1, colmun2 = st.columns((2,1))')
    with right_colmun:
        st.image(column2)
with st.container():
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('''- After created a column, you can use it by following the example :''')
    with right_colmun:
        st.image(column_use)

#---turtorial4---
with st.container():
    st.write('---')
    st.header('4. Insert picture the webpage')
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.subheader('4.1. Install pillow')
        st.write('- Firstly install pillow, another useful framework for python.')
        st.write('- Open cmd and type down the following syntax then press enter.')
        st.code('pip insatll pillow', language = 'C')
    with right_colmun:
        st.subheader('4.2. Import pillow')
        st.write("- Open your project and using the following syntax :")
        st.code('from PIL import Image', language = 'python')
#---turtorial4.1---
with st.container():
    st.subheader('4.3. How to use pillow')
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('''- Firsty add picture to your project root directory.''')
    with right_colmun:
        st.markdown("<u>Example :<u/>",unsafe_allow_html=True)
        st.image(ex_pic1)
with st.container():
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('- Now create a path for the picture with the following syntax :')
        st.code('your_pic = Image.open("your_file_path")', language = 'python')
    with right_colmun:
        st.image(ex_pic2)
with st.container():
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('- To us the pciture use the following syntax :')
        st.code('st.Image(your_pic)', language = 'python')
    with right_colmun:
        st.image(ex_pic3)

#---turtorial5---
with st.container():
    st.write('---')
    st.header('5. Lottie animation')
    st.write('- lottie animation is one of the framework that can make your web site more interesting and a fun animation')
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.subheader('5.1. Install lottie framwork')
        st.write("- Type the following command to cmd then press enter:")
        st.code('pip install lottie', language = 'C')
    with right_colmun:
        st.subheader('5.2. Import lottie')
        st.write('- To import lottie to your project use : ')
        st.code('from streamlit_lottie import st_lottie', language = 'python')
with st.container():
    st.subheader('5.3. Set up lottie using local path')
    st.write('- Firstly import json to your root directroy with syntax :')
    st.code('import json', language = 'python')
    left_column, right_colmun = st.columns(2)

    with left_column:
        st.write('- Download lottie animation as json file from this [lottiefiles.com>](https://lottiefiles.com/featured)')
    with right_colmun:
        st.image(download_json)
with st.container():    
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('- Now add json file to your project root directory.')
    with right_colmun:
        st.image(json_dir)
with st.container():    
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('- Now add json file to your project root directory.')
    with right_colmun:
        st.image(json_dir)
with st.container():    
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('- After import necessary file, create a function for loading local json file using the following syntax :')
    with right_colmun:
        st.code('''def localjson( filepath = str ):
    with open(filepath, 'r') as f:
        return json.load(f)''')
with st.container():    
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('- Create a variable for your file : ')
    with right_colmun:
        st.code('header_pic = localjson("lottie/coding-slide.json")')
with st.container():    
    left_column, right_colmun = st.columns(2)
    with left_column:
        st.write('- Load json file : ')
    with right_colmun:
        st.code('st_lottie(header_pic)')

#---end---
with st.container():
    st.write('---')
    st_lottie(bye_pic, height=500)
    st.markdown('<p style=" text-align: center; font-size: 35px;">With this you should be able to create your first simple website.</p>', unsafe_allow_html=True)
    st.markdown('<p style=" text-align: center; font-size: 35px;">Have fun coding.</p>', unsafe_allow_html=True)
    
