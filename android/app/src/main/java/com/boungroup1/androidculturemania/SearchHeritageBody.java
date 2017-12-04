package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by user on 03/12/2017.
 */

public class SearchHeritageBody {

    @SerializedName("query")
    @Expose
    private String query;

    @SerializedName("filters")
    @Expose
    private SearchFilters filters;

    public SearchHeritageBody(String query, SearchFilters filters) {
        this.query = query;
        this.filters = filters;
    }

    public SearchHeritageBody(String query) {
        this.query = query;
    }


    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }

    public SearchFilters getFilters() {
        return filters;
    }

    public void setFilters(SearchFilters filters) {
        this.filters = filters;
    }

}
