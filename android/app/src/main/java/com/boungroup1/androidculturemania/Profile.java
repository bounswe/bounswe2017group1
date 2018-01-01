package com.boungroup1.androidculturemania;

import com.google.gson.annotations.SerializedName;

/**
 * Created by mehmetsefa on 24/10/2017.
 */

public class Profile {
    @SerializedName("id")
    private int id;

    @SerializedName("username")
    private String username;

    @SerializedName("location")
    private String location;

    @SerializedName("gender")
    private String gender;

    @SerializedName("photo_path")
    private String photo_path;

    public int getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public String getLocation() {
        return location;
    }

    public String getGender() {
        return gender;
    }

    public String getPhoto_path() {
        return photo_path;
    }

    public Profile(int id, String username, String location, String gender, String photo_path) {
        this.id = id;
        this.username = username;
        this.location = location;
        this.gender = gender;
        this.photo_path = photo_path;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void setPhoto_path(String photo_path) {
        this.photo_path = photo_path;
    }
}
