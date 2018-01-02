package com.boungroup1.androidculturemania;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by mustafa on 11/26/17.
 */

public class VoteBody {
    @SerializedName("value")
    @Expose
    private Boolean value;

    @SerializedName("heritage")
    @Expose
    private Integer heritage;

    public VoteBody(Boolean value, Integer heritage) {
        this.value = value;
        this.heritage = heritage;
    }

    public Boolean getValue() {
        return value;
    }

    public void setValue(Boolean value) {
        this.value = value;
    }

    public Integer getHeritage() {
        return heritage;
    }

    public void setHeritage(Integer heritage) {
        this.heritage = heritage;
    }
}
