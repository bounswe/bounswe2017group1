package com.boungroup1.androidculturemania;

import com.google.gson.annotations.SerializedName;

/**
 * Created by user on 24/10/2017.
 */

public class User {

    @SerializedName("username")
    private String username;

    @SerializedName("email")
    private String email;

    public String getEmail() {
        return email;
    }

    public String getUsername() {
        return username;
    }

    public User(String username, String email) {
        this.username = username;
        this.email = email;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}