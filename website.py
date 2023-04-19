# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:58:52 2023

@author: Admin
"""

import streamlit as st

def main():
    st.title("Automated dropcasting process")

    video_links = [
        {
            "title": "Video 1",
            "url": "https://www.youtube.com/watch?v=b3kMRvcjZIQ",
            "description": "Description for video 1."
        },
        {
            "title": "Video 2",
            "url": "https://www.youtube.com/watch?v=fDqDH5OBnF8",
            "description": "Description for video 2."
        },
        {
            "title": "Video 3",
            "url": "https://www.youtube.com/watch?v=b8KKdyae6aM",
            "description": "Description for video 3."
        },
        {
            "title": "Video 4",
            "url": "https://www.youtube.com/watch?v=pflk6gPsC2o",
            "description": "Description for video 3."
        },
        {
            "title": "Video 5",
            "url": "https://www.youtube.com/watch?v=j6QyzAHanO8",
            "description": "Description for video 3."
        }
    ]

    for video in video_links:
        st.header(video["title"])
        st.video(video["url"])
        st.write(video["description"])
        
        
    

if __name__ == "__main__":
    main()

