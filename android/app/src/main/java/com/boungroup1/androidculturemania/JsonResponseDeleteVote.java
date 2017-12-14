package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by mustafa on 12/14/17.
 */

public class JsonResponseDeleteVote {
    @SerializedName("upvote_count")
    @Expose
    private Integer upvote_count;

    @SerializedName("downvote_count")
    @Expose
    private Integer downvote_count;

    public Integer getUpvote_count() {
        return upvote_count;
    }

    public void setUpvote_count(Integer upvote_count) {
        this.upvote_count = upvote_count;
    }

    public Integer getDownvote_count() {
        return downvote_count;
    }

    public void setDownvote_count(Integer downvote_count) {
        this.downvote_count = downvote_count;
    }
}
