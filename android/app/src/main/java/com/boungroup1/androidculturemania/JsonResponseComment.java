package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.Date;

/**
 * Created by user on 29/11/2017.
 */

public class JsonResponseComment {

    @SerializedName("id")
    @Expose
    private int id;

    @SerializedName("is_owner")
    @Expose
    private boolean is_owner;

    @SerializedName("creator_image_path")
    @Expose
    private String creator_image_path;

    @SerializedName("creator_username")
    @Expose
    private String creator_username;

    @SerializedName("text")
    @Expose
    private String text;

    @SerializedName("creation_date")
    @Expose
    private Date creation_date;

    @SerializedName("update_date")
    @Expose
    private Date update_date;

    @SerializedName("heritage")
    @Expose
    private int heritage;

    @SerializedName("creator")
    @Expose
    private int creator;

    @SerializedName("parent_comment")
    @Expose
    private int parent_comment;

    public JsonResponseComment(int id, boolean is_owner, String creator_image_path, String creator_username, String text, Date creation_date, Date update_date, int heritage, int creator, int parent_comment) {
        this.id = id;
        this.is_owner = is_owner;
        this.creator_image_path = creator_image_path;
        this.creator_username = creator_username;
        this.text = text;
        this.creation_date = creation_date;
        this.update_date = update_date;
        this.heritage = heritage;
        this.creator = creator;
        this.parent_comment = parent_comment;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public boolean isIs_owner() {
        return is_owner;
    }

    public void setIs_owner(boolean is_owner) {
        this.is_owner = is_owner;
    }

    public String getCreator_image_path() {
        return creator_image_path;
    }

    public void setCreator_image_path(String creator_image_path) {
        this.creator_image_path = creator_image_path;
    }

    public String getCreator_username() {
        return creator_username;
    }

    public void setCreator_username(String creator_username) {
        this.creator_username = creator_username;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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

    public int getHeritage() {
        return heritage;
    }

    public void setHeritage(int heritage) {
        this.heritage = heritage;
    }

    public int getCreator() {
        return creator;
    }

    public void setCreator(int creator) {
        this.creator = creator;
    }

    public int getParent_comment() {
        return parent_comment;
    }

    public void setParent_comment(int parent_comment) {
        this.parent_comment = parent_comment;
    }
}
