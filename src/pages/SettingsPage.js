import React from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import TwoOptionRadioButton from "../components/utility/ViewRadioButton";
import { useState } from "react";
import { useEffect } from "react";
import axios from "axios";
import SettingsGroupCard from "../components/SettingsGroupCard";

export default function SettingsPage() {
  const [groups, setGroups] = useState([]);
  const [filter, setFilter] = useState("Myself");
  const [view, setView] = useState("");

  const fetchData = async () => {
    try {
      const groupsResponse = await axios.get(`/api/groups`);
      const filterResponse = await axios.get("/api/current_filter/setting");
      const viewResponse = await axios.get(`/api/view`);
      setGroups(groupsResponse.data);
      setFilter(filterResponse.data);
      setView(viewResponse.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const filterOptions = Object.entries(groups);
  filterOptions.unshift(["Myself", {}]);

  const cards = filterOptions.map((group, index) => {
    return (
      <SettingsGroupCard
        key={index}
        id={group[0]}
        members={group[1]}
        startState={group[0] === filter}
      />
    );
  });

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          <h2 id="settings-title">Settings</h2>
          {!(view === "") && (<TwoOptionRadioButton startState={view} />)}
          <div id="filter-type-section">
            <h2 id="settings-title">Filter out allergens by:</h2>
            <form id="settings-group-filter">{cards}</form>
          </div>
        </div>
      </div>
    </div>
  );
}
