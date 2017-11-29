package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by user on 30/11/2017.
 */

public class CommentBody {
    @SerializedName("text")
    @Expose
    public String text;
    @SerializedName("heritage")
    @Expose
    public int heritage;

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getHeritage() {
        return heritage;
    }

    public void setHeritage(int heritage) {
        this.heritage = heritage;
    }

    public CommentBody(String text, int heritage) {
        this.text = text;
        this.heritage = heritage;
    }
}
