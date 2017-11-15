package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

/**
 * Created by tahabayi on 15/11/2017.
 */

public class JsonResponseHeritage {

    class tags{

        @SerializedName("id")
        @Expose
        private int id;

        @SerializedName("name")
        @Expose
        private String name;

        @SerializedName("category")
        @Expose
        private String category;

        public tags(int id, String name, String category ) {
            this.id = id;
            this.name = name;
            this.category = category;
        }

        public int getId() {
            return id;
        }

        public void setId(int id) {
            this.id = id;
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

    @SerializedName("id")
    @Expose
    private int id;

    @SerializedName("upvote_count")
    @Expose
    private int upvote_count;

    @SerializedName("downvote_count")
    @Expose
    private int downvote_count;

    @SerializedName("tags")
    @Expose
    private List<tags> tags;

    @SerializedName("title")
    @Expose
    private String title;

    @SerializedName("description")
    @Expose
    private String description;

    @SerializedName("creation_date")
    @Expose
    private String creation_date;

    @SerializedName("event_date")
    @Expose
    private String event_date;

    @SerializedName("location")
    @Expose
    private String location;

    @SerializedName("creator")
    @Expose
    private int creator;


    public JsonResponseHeritage(int id, int upvote_count, int downvote_count, List<tags> tags, String title, String description, String creation_date, String event_date, String location, int creator ) {
        this.id = id;
        this.upvote_count = upvote_count;
        this.downvote_count = downvote_count;
        this.tags = tags;
        this.description = description;
        this.creation_date = creation_date;
        this.event_date = event_date;
        this.location = location;
        this.creator = creator;
        this.title = title;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getUpvote_count() {
        return upvote_count;
    }

    public void setUpvote_count(int upvote_count) {
        this.upvote_count = upvote_count;
    }

    public int getDownvote_count() {
        return downvote_count;
    }

    public void setDownvote_count(int downvote_count) {
        this.downvote_count = downvote_count;
    }

    public List<JsonResponseHeritage.tags> getTags() {
        return tags;
    }

    public void setTags(List<JsonResponseHeritage.tags> tags) {
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

    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
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

    public int getCreator() {
        return creator;
    }

    public void setCreator(int creator) {
        this.creator = creator;
    }

}
