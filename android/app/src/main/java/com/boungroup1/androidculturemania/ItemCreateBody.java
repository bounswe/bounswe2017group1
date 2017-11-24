package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

/**
 * Created by user on 12/11/2017.
 */

public class ItemCreateBody {
    @SerializedName("title")
    @Expose
    public String title;
    @SerializedName("description")
    @Expose
    public String description;
    @SerializedName("event_date")
    @Expose
    public String event_date;
    @SerializedName("location")
    @Expose
    public String location;
    @SerializedName("tags")
    @Expose
    public List<Tag> tags;

    public ItemCreateBody(String title, String description, String event_date, String location, List<Tag> tags) {
        this.title = title;
        this.description = description;
        this.event_date = event_date;
        this.location = location;
        this.tags = tags;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getEvent_date() {
        return event_date;
    }

    public void setEvent_date(String event_date) {
        this.event_date = event_date;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<Tag> getTags() {
        return tags;
    }

    public void setTags(List<Tag> tags) {
        this.tags = tags;
    }
}
