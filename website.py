# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:58:52 2023

@author: Admin
"""

import streamlit as st


def main():
    st.title("Case study: debugging a “simple” drop-casting process on carbon paper")
    
    st.markdown('''
                As stated in the main body, it is a common expectation that automated experiment platforms will readily deliver reproducible results. However, in reality, this is often not the case. A controlled level of noise can only be attained through a meticulous analysis of each stage of the pipeline. Here, we will use the drop-casting step in our experimental workflow as a case study.
                
                '''
                )
    st.markdown("# Background")
    st.markdown('''
                There are plenty of methods to load the active materials onto a conductive substrate to make a heterogeneous electrochemistry catalyst. In our lab, the active materials are multiple metal salts (e.g. FeCl3, Cu(NO3)2) dissolved in ethanol, and the substrate is a commercial carbon thin film. We are using Opentrons to handle all the precursor mixing jobs, as well as the final drop-casting step, which can be illustrated in FIG S1. From a manual experiment perspective, this step cannot be even simpler, a bunch of operations are surely more complex than this one. However, lots of issues will just arise once we attempt to automate this process in a high-throughput manner. Supplementary video 1 shows the preliminary results, which apparently deliver inconsistent wetting behavior and sample size. 
                ''')
                
                
    
    # Figure 1
    
    st.image("https://imgur.com/ju0Zql0.png",
             width = 500,
             caption="Figure S1: The drop-casting method is adopted in our lab to prepare electrocatalyst samples. Despite its seemingly simple appearance, automating this process for high-throughput purposes can present significant challenges.")
    
    st.markdown("## Objectives")
    st.markdown('''
                The objectives are mainly two folds: (i) the catalyst materials are well dispersed into the carbon substrate, so that the metal elements are well utilized, and (ii) the catalyst footprint areas are identical across samples, since it’s a convention to normalize the performance (current density - mA/cm2) based on this number. Seemingly straightforward, it actually took us about 3 months to make this automated workflow “work”, as shown in Supplementary Video 2.
                '''
                )
    st.markdown("## Discussions")
    
    st.markdown('''
                There are way more issues than we expected beneath this simple looking process. To achieve a satisfactory drop casting process, a thorough analysis of almost all the components are necessary. The subsequent paragraphs highlight three primary concerns that significantly contribute to the variability of the final results.
                '''
                )
    
    st.markdown("### Wettability issue")
    
    st.markdown('''
                The wet-proofing layer determines the dispersion of the precursor solution. Even a low percentage of wet-proofing (e.g. 5%) can result in poor wetting of the carbon by the ethanol, causing droplets to sit on the substrate for a period of time. This can lead to non-uniform distribution, as evidenced by the coffee ring effect in the samples shown in the second row of FIG S2a. The concentration in the outer circle is significantly higher than in the middle region, which is highly unfavorable. Furthermore, the wet-proofing layer may be unevenly distributed across the sample due to manufacturing imperfections, as demonstrated in Supplementary Video 1. In some areas, the carbon wets the ethanol immediately, while in others, the ethanol beads up before wetting. This inconsistency can result in uneven dispersion of the catalyst and varying footprint sizes across samples.

We then switched to the carbon paper with no wet-proofing layer, but immediately another issue came up. Following the completion of the drop-casting process, some yellowish stain appeared on the heat stage, as illustrated in FIG S2b. Repeated experiments confirmed these stains are leaked precursor solutions. Our analysis is that, in the absence of a wet-proofing layer, the carbon readily absorbs the ethanol, which can then penetrate to the bottom surface of the carbon strip due to gravity. When the carbon comes into contact with the heat stage, the liquid can be “pulled out” of the carbon strip, leading to the issue of leakage. Since the amount of loss cannot be controlled, the catalyst loading of each sample becomes quite different. To resolve this issue, a zig-zag shaped stage was designed and 3d-printed (FIG S2c), which eliminates physical contact at the drop-casting spots (FIG S2d). In this manner, the precursors can be well retained within the carbon strip, and no leakage occurs.
                ''')
     # Figure 1
     
    st.image("https://imgur.com/3WuwoNv.png",
              
              caption="Figure S2: (a) Serious coffee ring effect will show up if a carbon paper with wet-proofing layer is used as substrate, leading to non-uniform distribution of active materials. (b) On the other hand, the ethanol-based precursor can penetrate through the carbon paper with no wet-proofing layer, subsequently seeping onto the heat stage upon contact, as evidenced by the yellowish stain around the 2nd-row carbon strip. (c)  a zig-zag shaped sample stage was designed and 3d-printed to resolve the precursor leakage issue. (d) The customized stage provides no physical contact at the drop-casting spot, ensuring that the precursor solution remains within the carbon substrate."              )
                
     
    
    
    st.markdown("### Non Ideal geometry of carbon substrate")
    st.markdown('''
               The carbon substrate cut from a commercial 10cm by 10cm sheet may not always be perfectly flat, as it can have some inherent curvature and cutting-induced twist. This issue was recognized after observing a wired phenomenon in some samples, e.g. in Supplementary Video 3 (carbon strip indexed from 1-6 from left to right), we can see (i) no precursor foot print on #6 carbon strip, and (ii) there are regular footprints in #4 and #5 in the first 4 drop-casts while the last one is missing. Initially, we attributed this to the non-uniformity of the carbon paper, but later we realized that it’s owing to the intrinsic curvature of the carbon paper strip. As shown in FIG S2a, the pipette tip's height was set at the same level across the entire strip, while the carbon was not perfectly flat in this range. As a result, the pipette tip would make good contact with the carbon in the middle region, while the droplet will dangle on the tip near the edge, giving no precursor footprint on the carbon substrate. This hypothesis was confirmed through a closer observation in Supplementary Video 4. However, lowering the height of the pipetting tip recklessly could result in experiment accidents, such as piercing through and even dragging the carbon substrate, as shown in Supplementary Video 5. The discovery of this issue is asking us to carefully tune the height of the pipette tip, down to 100μm interval (the thickness of the carbon strip varies between 100~400μm). 

Besides, some local tilt can also affect the shape of the footprint. Instead of being dispersed isotropically, the precursor will diffuse primarily in a particular direction driven by gravity. As shown in FIG S3b, the upper half of the sample in the first carbon strip displays a darker color due to a local incline towards the up side. These results reminded us to control the cutting process as well, which could affect the deformation of the length edge of the carbon strip. The substitution of a lab scissor with a large paper trimmer significantly relieved this issue.
                '''
                )
    
    st.image("https://imgur.com/ScCpSjK.png",
              
              caption="Figure S3: (a) A scheme aiming to account for the absence of a drop-casting footprint near the edge occasionally, as observed in Supplementary Video 3. As the height of the pipette tip is fixed across the entire strip, any inherent curvature in the carbon substrate can cause the droplet to be suspended on the tip without coming into contact with the carbon near the edge, which is evidenced in Supplementary Video 4. (b) Uneven distribution of the catalyst can also result from local tilt, as seen in the first carbon strip where the upper half appears darker due to a local incline towards the up side.")
    
    st.markdown("### Diffusion-driven cross contamination")
    st.markdown('''
               In most cases, the goal is to drop-cast as quickly as possible to reduce ethanol solvent evaporation and save time. However, it has been observed that if the drop-casting rate is too fast, the precursor can diffuse over a longer distance and potentially contaminate neighboring samples, as seen in FIG S4a. Therefore, to achieve an ideal footprint geometry (a round spot with diameter ~10mm), the drop-casting rate needs to be carefully tuned, which is a variable dependent on the carbon paper thickness and sample stage temperature. 

Additionally, we discovered another intriguing factor: the carbon fiber in the carbon paper is not isotropic but has a dominant direction. We depicted a simplified schematic of a 10cm*10cm carbon paper sheet in FIG S4d, where the white horizontal lines represent the dominant direction of the carbon fibers. Since it’s anisotropic, there are two ways to cut the sheet into ten 1cm*10cm carbon strips, which we will refer to as “perpendicular cut” (FIG S4e) and “parallel cut” (FIG S4f), respectively. The samples prepared with these two cutting methods display different colors (depending on perspective), as shown in FIG S4b, carbon strip 1 is “perpendicular cut” and appears darker, while carbon strip 2 is “parallel cut” and appears brighter. After we drop-casted the precursor solution onto them, they exhibit distinct behavior in terms of liquid diffusion. FIG S4c (picture shot from side view for optimal footprint visualization) clearly illustrates that the footprints of both carbon strips tend to extend in the direction of their dominant fibers. Thus, the “perpendicular cut” method should be employed for all samples to minimize the risk of cross-contamination between neighboring samples.
                '''
                )
    
    st.image("https://imgur.com/PFOTW68.png",
              
              caption="Figure S4: (a) A high rate of pipetting can lead to expanded drop-casting footprint, increasing the likelihood of sample cross-contamination. Additionally, we have observed that the carbon strips cut using different methods (strip 1 with perpendicular cut, strip 2 with parallel cut) can exhibit variations in terms of (b) darkness and (c) precursor diffusion behavior. Carbon strip 2 prepared with “parallel cut” tends to produce a footprint that extends in its length direction, which increases the risk of cross-contamination and is therefore less desirable. (d) A commercial square-shaped carbon paper sheet is not isotropic regarding its carbon fiber alignment, and here, we denote the dominant direction with white lines. This anisotropy leads to two cutting approaches, (e) “perpendicular cut”, where we cut perpendicular to the dominant fiber direction and (f) “parallel cut”, where we cut parallel with the dominant fiber direction.")

    st.markdown("## Summary")
    st.markdown('''
               As mentioned in the main text, all the aforementioned issues may look trivial at first glance, while they only become trivial after we realize their existence. Before we take them under control, they are real challenges that could fail our active learning project. Taking the last issue as an example, as shown in FIG S4c, the carbon strips prepared with “parallel cut” method could deliver ~10% larger footprint area than that prepared with “perpendicular cut” method, which will lead to a nominal increase in electrocatalytic performance (even with a fixed catalyst loading, a larger sample area usually yields a higher current value). Without acknowledging the carbon paper is anisotropic, one would just perform the cutting process at will and obtain scattered results. If multiple issues like this one are not well controlled, they can accumulate and lead to a single phenomenon: we find the experiment “irreproducible”.
                '''
                )
    
    
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

