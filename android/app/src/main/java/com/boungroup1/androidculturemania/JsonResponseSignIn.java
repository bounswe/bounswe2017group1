package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Response of the Sign In Post Request
 */

public class JsonResponseSignIn {
    @SerializedName("token")
    @Expose
    private String token;

    public JsonResponseSignIn(String token) {
        this.token = token;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
}
