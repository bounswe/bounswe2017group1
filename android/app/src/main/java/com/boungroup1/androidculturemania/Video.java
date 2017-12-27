package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by tahabayi on 27/12/2017.
 */

public class Video {

    @SerializedName("heritage")
    @Expose
    public int heritage;

    @SerializedName("video_url")
    @Expose
    public String video_url;

    @SerializedName("creation_date")
    @Expose
    public String creation_date;

    @SerializedName("update_date")
    @Expose
    public String update_date;
}
