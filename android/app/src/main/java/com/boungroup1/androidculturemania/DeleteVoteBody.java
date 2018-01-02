package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by mustafa on 12/14/17.
 */

public class DeleteVoteBody {
    @SerializedName("heritage")
    @Expose
    private Integer heritage;

    public Integer getHeritage() {
        return heritage;
    }

    public void setHeritage(Integer heritage) {
        this.heritage = heritage;
    }

    public DeleteVoteBody(Integer heritage) {
        this.heritage = heritage;
    }
}
