package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by tahabayi on 04/12/2017.
 */

public class Media {

    @SerializedName("id")
    @Expose
    public int id;
    @SerializedName("heritage")
    @Expose
    public int heritage;
    @SerializedName("image")
    @Expose
    public String image;
    @SerializedName("creation_date")
    @Expose
    public String creation_date;
    @SerializedName("update_date")
    @Expose
    public String update_date;

    public Media(int id, int heritage, String image, String creation_date, String update_date) {
        this.id = id;
        this.heritage = heritage;
        this.image = image;
        this.creation_date = creation_date;
        this.update_date = update_date;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getHeritage() {
        return heritage;
    }

    public void setHeritage(int heritage) {
        this.heritage = heritage;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
    }

    public String getUpdate_date() {
        return update_date;
    }

    public void setUpdate_date(String update_date) {
        this.update_date = update_date;
    }

}
