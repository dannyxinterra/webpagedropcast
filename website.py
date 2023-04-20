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


def add_video(video_url, caption):
    pass


def main():
    st.title(ct.title)

    st.markdown(ct.intro)

    st.header("Background")
    st.markdown(ct.background)

    # Figure 1
    add_fig(ct.fig_urls[0], ct.fig_caps[0])

    st.header("Objectives")
    st.markdown(ct.objectives)

    st.header("Discussions")
    st.markdown(ct.discussions)

    st.subheader("Wettability issue")
    st.markdown(ct.wettability_issue)

    # Figure 2
    add_fig(ct.fig_urls[1], ct.fig_caps[1])

    st.subheader("Non Ideal geometry of carbon substrate")
    st.markdown(ct.non_ideal_geometry)

    # Figure 3
    add_fig(ct.fig_urls[2], ct.fig_caps[2])

    st.subheader("Diffusion-driven cross contamination")
    st.markdown(ct.cross_contamination)

    # Figure 4
    add_fig(ct.fig_urls[3], ct.fig_caps[3])

    st.header("Summary")
    st.markdown(ct.summary)

    for video in ct.video_links:
        st.header(video["title"])
        st.video(video["url"])
        st.write(video["description"])


if __name__ == "__main__":
    main()
