package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by user on 24/10/2017.
 */

public class JsonResponseSignUp {
    @SerializedName("user")
    @Expose
    private User user;

    @SerializedName("token")
    @Expose
    private String token;

    @SerializedName("profile")
    @Expose
    private Profile profile;

    public User getUser() {
        return user;
    }

    public Profile getProfile() {
        return profile;
    }

    public JsonResponseSignUp(Profile profile,User user ) {
        this.user = user;
        this.profile = profile;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
}
