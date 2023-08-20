import base64

import streamlit as st


def render_svg(svg: str) -> None:
    """
    Render the given SVG string as an image.

    This function takes an SVG string, encodes it to base64, and then
    renders it as an image using Streamlit's write function. The image
    is embedded directly into the HTML using a data URL.

    Parameters
    ----------
    svg : str
        The SVG string to render.

    Returns
    -------
    None

    References
    ----------
    Borrowed From:
    https://gist.github.com/treuille/8b9cbfec270f7cda44c5fc398361b3b1
    """
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
    st.write(html, unsafe_allow_html=True)
