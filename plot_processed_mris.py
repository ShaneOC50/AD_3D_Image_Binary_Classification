import time

from skimage import io
import imageio
import numpy as np
import scipy

data_npy = '/home/shane/Thesis/git/Masked_Dataset/Masked_Data/OASIS_Mask/processed_data/2_OAS1_0240_MR1_mpr_n3_anon_111_t88_masked_gfc.npy'
t_vol = np.load(data_npy,allow_pickle=True)
print(t_vol[0].shape)
print(len(np.asarray(t_vol[0])))
tif_path = '/home/shane/Thesis/git/Dataset/0_OAS1_0001_MR1_mpr_n4_anon_111_t88_masked_gfc.tif'
mat_path = '/home/shane/Thesis/git/Dataset/2_OAS1_0240_MR1_mpr_n3_anon_111_t88_masked_gfc.mat'
scipy.io.savemat(mat_path,{"img":np.asarray(t_vol[0])})
# imageio.imwrite(tif_path,t_vol)
#scipy.misc.imsave(tif_path,data_npy)
#vol = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")
# vol = io.imread(tif_path)
# volume = vol.T\
volume = t_vol[0]
r, c = volume[0].shape

# Define frames
import plotly.graph_objects as go
nb_frames = 68

fig = go.Figure(frames=[go.Frame(data=go.Surface(
    z=(6.7 - k * 0.1) * np.ones((r, c)),
    surfacecolor=np.flipud(volume[67 - k]),
    cmin=0, cmax=200
    ),
    name=str(k) # you need to name the frame for the animation to behave properly
    )
    for k in range(nb_frames)])

# Add data to be displayed before animation starts
fig.add_trace(go.Surface(
    z=6.7 * np.ones((r, c)),
    surfacecolor=np.flipud(volume[67]),
    colorscale='Gray',
    cmin=0, cmax=200,
    colorbar=dict(thickness=20, ticklen=4)
    ))


def frame_args(duration):
    return {
            "frame": {"duration": duration},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
        }

sliders = [
            {
                "pad": {"b": 10, "t": 60},
                "len": 0.9,
                "x": 0.1,
                "y": 0,
                "steps": [
                    {
                        "args": [[f.name], frame_args(0)],
                        "label": str(k),
                        "method": "animate",
                    }
                    for k, f in enumerate(fig.frames)
                ],
            }
        ]

# Layout
fig.update_layout(
         title='Slices in volumetric data',
         width=600,
         height=600,
         scene=dict(
                    zaxis=dict(range=[-0.1, 6.8], autorange=False),
                    aspectratio=dict(x=1, y=1, z=1),
                    ),
         updatemenus = [
            {
                "buttons": [
                    {
                        "args": [None, frame_args(50)],
                        "label": "&#9654;", # play symbol
                        "method": "animate",
                    },
                    {
                        "args": [[None], frame_args(0)],
                        "label": "&#9724;", # pause symbol
                        "method": "animate",
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 70},
                "type": "buttons",
                "x": 0.1,
                "y": 0,
            }
         ],
         sliders=sliders
)

fig.show()