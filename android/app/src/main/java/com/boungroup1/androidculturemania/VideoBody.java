package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by tahabayi on 27/12/2017.
 */

public class VideoBody {
    @SerializedName("video_url")
    @Expose
    public String video_url;
    @SerializedName("heritage")
    @Expose
    public int heritage;

    public String getText() {
        return video_url;
    }

    public void setText(String video_url) {
        this.video_url = video_url;
    }

    public int getHeritage() {
        return heritage;
    }

    public void setHeritage(int heritage) {
        this.heritage = heritage;
    }

    public VideoBody(String video_url, int heritage) {
        this.video_url = video_url;
        this.heritage = heritage;
    }
}
