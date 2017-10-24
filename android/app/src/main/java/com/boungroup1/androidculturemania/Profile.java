package com.boungroup1.androidculturemania;

import com.google.gson.annotations.SerializedName;

/**
 * Created by user on 24/10/2017.
 */

public class Profile {
    @SerializedName("id")
    private int id;

    @SerializedName("username")
    private String username;

    @SerializedName("locatin")
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
}
