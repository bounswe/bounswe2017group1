package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.Date;

/**
 * Created by mustafa on 11/26/17.
 */

public class JsonResponseVote {
    @SerializedName("id")
    @Expose
    private Integer id;

    @SerializedName("value")
    @Expose
    private Boolean value;

    @SerializedName("creation_date")
    @Expose
    private Date creation_date;

    @SerializedName("update_date")
    @Expose
    private Date update_date;

    @SerializedName("voter")
    @Expose
    private Integer voter;

    @SerializedName("heritage")
    @Expose
    private Integer heritage;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Boolean getValue() {
        return value;
    }

    public void setValue(Boolean value) {
        this.value = value;
    }

    public Date getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(Date creation_date) {
        this.creation_date = creation_date;
    }

    public Date getUpdate_date() {
        return update_date;
    }

    public void setUpdate_date(Date update_date) {
        this.update_date = update_date;
    }

    public Integer getVoter() {
        return voter;
    }

    public void setVoter(Integer voter) {
        this.voter = voter;
    }

    public Integer getHeritage() {
        return heritage;
    }

    public void setHeritage(Integer heritage) {
        this.heritage = heritage;
    }
}
