package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.Date;
import java.util.List;

/**
 * Created by user on 23/11/2017.
 */

public class JsonResponseItemDetail {
    @SerializedName("id")
    @Expose
    private int id;

    @SerializedName("upvote_count")
    @Expose
    private int upvote_count;

    @SerializedName("downvote_count")
    @Expose
    private int downvote_count;

    @SerializedName("is_upvoted")
    @Expose
    private boolean is_upvoted;

    @SerializedName("is_downvoted")
    @Expose
    private boolean is_downvoted;

    @SerializedName("tags")
    @Expose
    private List<TagResponse> tags;

    @SerializedName("title")
    @Expose
    private String title;

    @SerializedName("description")
    @Expose
    private String description;

    @SerializedName("creation_date")
    @Expose
    private Date creation_date;

    @SerializedName("event_date")
    @Expose
    private Date event_date;

    @SerializedName("location")
    @Expose
    private String location;

    @SerializedName("creator")
    @Expose
    private int creator;

    @SerializedName("creator_username")
    @Expose
    private String creator_username;

    @SerializedName("creator_image_path")
    @Expose
    private String creator_image_path;

    @SerializedName("medias")
    @Expose
    private List<Media> media;

    public Video getVideo() {
        return video;
    }

    public void setVideo(Video video) {
        this.video = video;
    }

    @SerializedName("video")
    @Expose
    private Video video;

    public String getCreator_image_path() {
        return creator_image_path;
    }

    public void setCreator_image_path(String creator_image_path) {
        this.creator_image_path = creator_image_path;
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

    public List<TagResponse> getTags() {
        return tags;
    }

    public boolean isIs_upvoted() {
        return is_upvoted;
    }

    public void setIs_upvoted(boolean is_upvoted) {
        this.is_upvoted = is_upvoted;
    }

    public boolean isIs_downvoted() {
        return is_downvoted;
    }

    public void setIs_downvoted(boolean is_downvoted) {
        this.is_downvoted = is_downvoted;
    }

    public void setTags(List<TagResponse> tags) {
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

    public Date getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(Date creation_date) {
        this.creation_date = creation_date;
    }

    public Date getEvent_date() {
        return event_date;
    }

    public void setEvent_date(Date event_date) {
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

    public String getCreator_username() {
        return creator_username;
    }

    public void setCreator_username(String creator_username) {
        this.creator_username = creator_username;
    }

    public List<Media> getMedia() {
        return media;
    }

    public void setMedia(List<Media> media) {
        this.media = media;
    }
}
