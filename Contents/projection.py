import yt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

def label(proj):
    if proj == 'x':
        x_str = 'y (Mpc)'
        y_str = 'z (Mpc)'
    elif proj == 'y':
        x_str = 'z (Mpc)'
        y_str = 'x (Mpc)'
    else:
        x_str = 'x (Mpc)'
        y_str = 'y (Mpc)'
    return x_str,y_str

def sliced(axis,m_cube,slc_num,title):
    h = 0.7
    H_scale = 2 / h
    if axis == "z":
        m_2d = m_cube[:,:,[slc_num]]
    elif axis == "y":
        m_2d = m_cube[:, [slc_num],:].squeeze()
    else:
        m_2d = m_cube[[slc_num],:,:].squeeze()

    fig, ax = plt.subplots(figsize=(10,10))
    im = ax.imshow(m_2d, origin="lower", extent=[-(H_scale / 2), H_scale / 2, -(H_scale / 2), H_scale / 2])
    plt.close()
    ax.set_xlabel(label(axis)[0],fontsize=20,**{'fontname':'Times New Roman'})
    ax.set_ylabel(label(axis)[1],fontsize=20,**{'fontname':'Times New Roman'})
    ax.set_title(title,fontsize=25,**{'fontname':'Times New Roman'})
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.0)
    cb = fig.colorbar(im,cax = cax)
    cb.set_label('$\mathcal{M}$',size=20)
    cb.ax.tick_params(labelsize=20)
    for l in cb.ax.yaxis.get_ticklabels():
        l.set_family("Times New Roman")
    return fig
def projected(axis,m_cube,title):
    h = 0.7
    H_scale = 2 / h
    weights = np.ones((256, 256, 256))
    weights[np.where(m_cube < 1)] = 1e-16
    frame = np.zeros((256,256))
    if axis == "z":
        for i in range(0,256):
            for j in range(0,256):
                m_ij = np.array(m_cube[i,j,::])
                w_ij = np.array(weights[i,j,::])
                summed = np.sum(m_ij*w_ij)
                m_ave = summed / (np.sum(w_ij))
                frame[j, i] = m_ave
    elif axis == "y":
        for i in range(0,256):
            for j in range(0,256):
                m_ij = np.array(m_cube[j,::,i])
                w_ij = np.array(weights[j,::,i])
                summed = np.sum(m_ij*w_ij)
                m_ave = summed / (np.sum(w_ij))
                frame[j, i] = m_ave
    else:
        for i in range(0,256):
            for j in range(0,256):
                m_ij = np.array(m_cube[::,i,j])
                w_ij = np.array(weights[::,i,j])
                summed = np.sum(m_ij*w_ij)
                m_ave = summed / (np.sum(w_ij))
                frame[j,i] = m_ave

    fig, ax = plt.subplots(figsize=(10,10))
    im = ax.imshow(frame, origin="lower", extent=[-(H_scale / 2), H_scale / 2, -(H_scale / 2), H_scale / 2])
    plt.close()
    ax.set_xlabel(label(axis)[0],fontsize=20,**{'fontname':'Times New Roman'})
    ax.set_ylabel(label(axis)[1],fontsize=20,**{'fontname':'Times New Roman'})
    ax.set_title(title,fontsize=25,**{'fontname':'Times New Roman'})
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.0)
    cb = fig.colorbar(im,cax = cax)
    cb.set_label('$\mathcal{M}$',size=20)
    cb.ax.tick_params(labelsize=20)
    for l in cb.ax.yaxis.get_ticklabels():
        l.set_family("Times New Roman")
    return fig
#def projected(axis,m_cube,r200c=False):
    #h = 0.7
   # H_scale = 2 / h

    #weights = np.ones((256, 256, 256))
    #weights[np.where(m_cube < 1)] = 1e-16

    #data = dict(m_cube=(m_cube, ""),weights=(weights,""))
    #bbox = np.array([[-(H_scale / 2), H_scale / 2], [-H_scale / 2, H_scale / 2], [-H_scale / 2, H_scale / 2]])
    #frame = yt.load_uniform_grid(data, domain_dimensions=m_cube.shape, length_unit='Mpc', bbox=bbox)
    #Slc = yt.ProjectionPlot(frame, axis, "m_cube",weight_field="weights")
    #Slc.set_cmap('m_cube', 'terrain')
    #Slc.set_log('m_cube', False)
    #Slc.set_xlabel(label(axis)[0])
    #Slc.set_ylabel(label(axis)[1])
    #Slc.set_width((H_scale, 'Mpc'))
    #Slc.set_colorbar_label('m_cube', 'Average $\mathcal{M}$')
    #if 0.85 * np.max(m_cube) >= 1.1:
        #max_lim = 0.7 * np.max(m_cube)
    #else:
        #max_lim = 1.1
    #Slc.set_zlim("m_cube", 1, max_lim)
    #Slc.set_font_size(24)
    #if r200c == True:
        #
    #return Slc
