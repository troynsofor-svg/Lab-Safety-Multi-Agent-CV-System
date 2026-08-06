while True:
    frame = cam.read()
    scene_msg = perception_agent.process_frame(frame)
    log_handoff("perception → safety", scene_msg)

    decision_msg = safety_agent.evaluate(scene_msg)
    log_handoff("safety → orchestrator", decision_msg)

    execute_actions(decision_msg)

