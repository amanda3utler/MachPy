import streamlit as st
from Contents import extract_halo, set_lw, sliced, projected

st.sidebar.title("MachPy")

if 'haloid' not in st.session_state:
    st.session_state['haloid'] = "1"

if 'lw' not in st.session_state:
    st.session_state['lw'] = 1.0

if 'slc' not in st.session_state:
    st.session_state['slc'] = 1

haloid = st.sidebar.text_input("Halo ID",value=st.session_state.haloid)

@st.cache
def get_ID(haloid,lw):
    mach_data = set_lw(cutoff=lw, ndin=extract_halo(haloid_path=head + str(haloid) + end))
    return mach_data

lw = st.sidebar.slider('Lower Cutoff',0.0,3.0,value=st.session_state.lw,step=0.1)

select = st.sidebar.selectbox("Type",("Slice","Projection"))
axe = st.sidebar.selectbox("Axis",("x","y","z"))

head = "Contents/cubedat/M_L7_"
end = ".npy"
#mach_data = set_lw(cutoff=lw,ndin=extract_halo(haloid_path=head+str(haloid)+end))
mach_data = get_ID(haloid=haloid,lw=lw)
slc = st.sidebar.slider('Slice', 0, 256, value=st.session_state.slc, step=1)

if select == "Slice":
    title = "CL" + haloid + " Slice (" + str(axe) + ", "+str(slc)+")"
    Slc = sliced(axis=axe,m_cube=mach_data,slc_num=slc,title=title)
    file_name = "CL"+haloid+"LW"+str(lw)+axe+str(slc)+".png"

if select == "Projection":
    title = "CL"+haloid+" Projection ("+str(axe)+")"
    Slc = projected(axis=axe,m_cube=mach_data,title=title)
    file_name = "CL"+haloid+"LW"+str(lw) + axe +"proj.png"

st.pyplot(Slc)
Slc.savefig("Mach.png")
with open("Mach.png", "rb") as file:
    btn = st.download_button(
        label="Download as PNG",
        data=file,
        file_name=file_name,
        mime="image/png"
    )
