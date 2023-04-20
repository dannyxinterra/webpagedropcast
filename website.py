# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:58:52 2023

@author: Admin
"""

import streamlit as st
import content as ct


def add_fig(fig_url, fig_cap, width=100):
    st.markdown(
        f"<div style='text-align: center;'><img src='{fig_url}' style='max-width: {width}%; height: auto;'/></div>",
        unsafe_allow_html=True,
    )
    st.caption(fig_cap)


def add_video(vid_url, vid_cap):
    st.video(vid_url)
    st.caption(vid_cap)


def create_link(text):
    # remove spaces and special characters from the text
    link_text = text.lower().replace(" ", "-").replace(".", "")
    # return the hyperlink
    return f"<a style='text-decoration:none; color:#333' href='#{link_text}'>{text}</a>"


def header_sidebar(text, subheaders=None):
    if subheaders:
        return f"<li>{create_link(text)}<ul>{''.join([subheader_sidebar(text) for text in subheaders])}</ul></li>"
    return f"<li>{create_link(text)}</li>"


def subheader_sidebar(text):
    return f"<li>{create_link(text)}</li>"



def main():
    st.title(ct.title)

    st.write('')

    st.caption(ct.author, unsafe_allow_html=True)

    st.markdown(ct.intro)

    # Figure 1
    add_fig(ct.fig_urls[0], ct.fig_caps[0])

    st.header("Background")
    st.markdown(ct.background, unsafe_allow_html=True)

    # Video 1
    add_video(ct.vid_urls[0], ct.vid_caps[0])

    st.header("Objectives")
    st.markdown(ct.objectives, unsafe_allow_html=True)

    # Video 2
    add_video(ct.vid_urls[1], ct.vid_caps[1])

    st.header("Discussions")
    st.markdown(ct.discussions)

    st.subheader("Wettability issue")
    st.markdown(ct.wettability_issue)

    # Figure 2
    add_fig(ct.fig_urls[1], ct.fig_caps[1])

    st.subheader("Non Ideal geometry of carbon")
    st.markdown(ct.non_ideal_geometry_1)

    # Video 3
    add_video(ct.vid_urls[2], ct.vid_caps[2])

    st.markdown(ct.non_ideal_geometry_2)

    # Figure 3
    add_fig(ct.fig_urls[2], ct.fig_caps[2])

    # Video 4
    add_video(ct.vid_urls[3], ct.vid_caps[3])

    # Video 5
    add_video(ct.vid_urls[4], ct.vid_caps[4])

    st.subheader("Diffusion-driven cross contamination")
    st.markdown(ct.cross_contamination)

    # Figure 4
    add_fig(ct.fig_urls[3], ct.fig_caps[3])

    st.header("Summary")
    st.markdown(ct.summary)

    # Outline sidebar
    subheaders = ["Wettability issue", "Non Ideal geometry of carbon", "Diffusion-driven cross contamination"]
    st.sidebar.markdown("# Outline")
    st.sidebar.markdown(f"<ul> "
                        f"{header_sidebar('Background')}"
                        f"{header_sidebar('Objectives')}"
                        f"{header_sidebar('Discussions', subheaders=subheaders)}"
                        f"{header_sidebar('Summary')}"
                        f"</ul>",
                        unsafe_allow_html=True)


if __name__ == "__main__":
    main()
