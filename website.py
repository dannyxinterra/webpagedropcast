# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:58:52 2023

@author: Admin
"""

import streamlit as st
import content as ct


def add_image(image_url, caption, width=100):
    st.markdown(
        f"<div style='text-align: center;'><img src='{image_url}' style='max-width: {width}%; height: auto;'/></div>",
        unsafe_allow_html=True,
    )
    st.caption(caption)


def main():
    st.title(ct.title)

    st.markdown(ct.intro)

    st.header("Background")
    st.markdown(ct.background)

    # Figure 1
    add_image(ct.figure_1_url, ct.figure_1_cap)

    st.header("Objectives")
    st.markdown(ct.objectives)

    st.header("Discussions")
    st.markdown(ct.discussions)

    st.subheader("Wettability issue")
    st.markdown(ct.wettability_issue)

    # Figure 2
    add_image(ct.figure_2_url, ct.figure_2_cap)

    st.subheader("Non Ideal geometry of carbon substrate")
    st.markdown(ct.non_ideal_geometry)

    # Figure 3
    add_image(ct.figure_3_url, ct.figure_3_cap)

    st.subheader("Diffusion-driven cross contamination")
    st.markdown(ct.cross_contamination)

    # Figure 4
    add_image(ct.figure_4_url, ct.figure_4_cap)

    st.header("Summary")
    st.markdown(ct.summary)

    for video in ct.video_links:
        st.header(video["title"])
        st.video(video["url"])
        st.write(video["description"])


if __name__ == "__main__":
    main()
