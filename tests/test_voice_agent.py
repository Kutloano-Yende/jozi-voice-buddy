import voice_agent


def test_system_prompt_describes_jozi_buddy():
    assert "Jozi Buddy" in voice_agent.SYSTEM_PROMPT
    assert "Johannesburg" in voice_agent.SYSTEM_PROMPT


def test_build_agent_uses_nova_sonic_model():
    agent = voice_agent.build_agent()

    assert agent.model._config["model_id"] == voice_agent.MODEL_ID
    assert agent.model.region == voice_agent.REGION
