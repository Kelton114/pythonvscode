import streamlit as st
menu = st.sidebar.selectbox('Menu',['First Stage'])
if menu == 'First Stage':
        st.write('Too see the following context, Please enter the password')
        oneee, twooo, threeee = st.columns(3)
        with oneee:
            st.color_picker('1st digit','#DC1616')
        with twooo:
            st.color_picker('2nd digit','#1E4EFD')
        with threeee:
            st.color_picker('3rd digit','#17FF29')    
        cPassword = '321'
        cPassInput = st.text_input('Password Here',type='password')

        Submit = st.checkbox('Submit Color Password')
        if Submit:    
            if cPassInput:
                if cPassInput == cPassword:
                    st.sidebar.header('Stage 2')
                    onee,twoo,threee = st.sidebar.columns(3)
                    with onee:
                        one = st.checkbox('1')
                        four = st.checkbox('4')
                        seven = st.checkbox('7')
                    with twoo:
                        two = st.checkbox('2')
                        five = st.checkbox('5')
                        eight = st.checkbox('8')
                    with threee:
                        three = st.checkbox('3')
                        six = st.checkbox('6')
                        nine = st.checkbox('9')
                    Go = st.sidebar.checkbox('Submit Answer')
                    if Go:
                        if one and five and nine and six and four and not two and not three and not seven and not eight:
                            Lock = st.checkbox('NICE')
                            if Lock:
                                st.header('STAGE 3')
                                first = st.radio('1st Key',['True','False'],horizontal=True)
                                secound = st.radio('2nd Key',['True','False'],horizontal=True)
                                third = st.radio('3rd Key',['True','False'],horizontal=True)
                                if st.checkbox('Submit'):
                                    if first == 'True' and secound == 'False' and third == 'False':
                                        st.write('You made it!!')
                                        st.write('Yeah')
                                        st.write('Happy Birthday! Dad. I know this might not be the perfect website that you want, but i really did put a lot of effort in this, Do you enjoy it?')
                                        enjoy = st.radio('Do you enjoy it?',['Yes','No'])
                                        gogo = st.checkbox('SUBMIT')
                                        if gogo:
                                            if enjoy == 'Yes' or enjoy == 'YES':
                                                st.warning('Yeah, Happy Birthday dad. You are always the best dad, although you might not be an expert on expressing your love, i do really know you love me, i love you too dad. Happy Birthday')
                                            if enjoy == 'No':
                                                st.warning('You have one more chance')
                                                Extra = st.radio('Do you enjoy it?',['Yes','YES','No'])
                                                gggooo = st.checkbox('SUBmit')
                                                if gggooo == 'Yes' or Extra == 'YES':
                                                    st.warning('Yeah, Happy Birthday dad. You are always the best dad, although you might not be an expert on expressing your love, i do really know you love me, i love you too dad. Happy Birthday')
                                                if Extra == 'No':
                                                    st.warning('I do not care, you enjoyed it, yay. Yeah, Happy Birthday dad. You are always the best dad, although you might not be an expert on expressing your love, i do really know you love me, i love you too dad. Happy Birthday')
                                    else:
                                        st.warning('Wrong Password')
                        else:
                            st.sidebar.warning('Wrong Password')
                else:
                    st.write('Wrong Password')
            else:
                st.write('Please Enter Password')