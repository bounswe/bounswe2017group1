package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.Date;

/**
 * Created by mehmetsefa on 03/12/2017.
 */

public class SearchFilters {

    @SerializedName("location")
    @Expose
    private String location;

    @SerializedName("creator")
    @Expose
    private String creator;

    @SerializedName("creation_start")
    @Expose
    private Date creation_start;

    @SerializedName("creation_end")
    @Expose
    private Date creation_end;

    @SerializedName("event_start")
    @Expose
    private Date event_start;

    @SerializedName("event_end")
    @Expose
    private Date event_end;

    public SearchFilters(String location, String creator, Date creation_start, Date creation_end, Date event_start, Date event_end) {
        this.location = location;
        this.creator = creator;
        this.creation_start = creation_start;
        this.creation_end = creation_end;
        this.event_start = event_start;
        this.event_end = event_end;
    }

    public SearchFilters() {
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }

    public Date getCreation_start() {
        return creation_start;
    }

    public void setCreation_start(Date creation_start) {
        this.creation_start = creation_start;
    }

    public Date getCreation_end() {
        return creation_end;
    }

    public void setCreation_end(Date creation_end) {
        this.creation_end = creation_end;
    }

    public Date getEvent_start() {
        return event_start;
    }

    public void setEvent_start(Date event_start) {
        this.event_start = event_start;
    }

    public Date getEvent_end() {
        return event_end;
    }

    public void setEvent_end(Date event_end) {
        this.event_end = event_end;
    }
}
