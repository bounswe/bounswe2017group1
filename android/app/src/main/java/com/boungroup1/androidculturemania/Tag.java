package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by user on 12/11/2017.
 */

public class Tag {
//    @SerializedName("id")
//    @Expose
//    public int id;
    @SerializedName("name")
    @Expose
    public String name;
    @SerializedName("category")
    @Expose
    public String category;

    public Tag(String name, String category) {
        this.name = name;
        this.category = category;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
}
